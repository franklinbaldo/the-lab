-- astro-compat.lua
-- Pandoc Lua filter that converts LaTeX constructs into
-- Astro/GFM-compatible markdown.
--
-- Handles:
--   ::: center        -> <div style="text-align:center">
--   ::: thebibliography -> ## References section
--   ::: {#tab:...}    -> table wrapper (tables already GFM via -t gfm)
--   ::: {.definition}  -> blockquote with bold label
--   ::: {.conjecture}  -> blockquote with bold label
--   ::: {.openproblem} -> blockquote with bold label
--   ::: {.protocol}    -> blockquote with bold label
--   ::: epigraph       -> blockquote
--   ::: description    -> definition list as plain text
--   Cross-references   -> plain markdown links

-- Convert Div elements (Pandoc's representation of ::: blocks)
function Div(el)
  local id = el.identifier or ""
  local classes = el.classes or {}

  -- ::: center -> HTML centered div
  if classes:includes("center") then
    local blocks = el.content
    table.insert(blocks, 1, pandoc.RawBlock("html", '<div style="text-align:center">'))
    table.insert(blocks, pandoc.RawBlock("html", '</div>'))
    return blocks
  end

  -- ::: thebibliography -> References heading + content
  if classes:includes("thebibliography") then
    local blocks = pandoc.List({pandoc.Header(2, "References")})
    blocks:extend(el.content)
    return blocks
  end

  -- ::: epigraph -> blockquote
  if classes:includes("epigraph") then
    return pandoc.List({pandoc.BlockQuote(el.content)})
  end

  -- ::: description -> just pass through content
  if classes:includes("description") then
    return el.content
  end

  -- Labeled environments: definition, conjecture, openproblem, protocol
  local env_labels = {
    definition = "Definition",
    conjecture = "Conjecture",
    openproblem = "Open Problem",
    protocol = "Protocol",
  }

  for cls, label in pairs(env_labels) do
    if classes:includes(cls) then
      -- Wrap in a blockquote with a bold label prefix
      local header_inlines = pandoc.List({
        pandoc.Strong(pandoc.List({pandoc.Str(label)})),
      })
      if id ~= "" then
        header_inlines:insert(1, pandoc.RawInline("html", '<span id="' .. id .. '"></span>'))
      end
      local header = pandoc.Para(header_inlines)
      local blocks = pandoc.List({header})
      blocks:extend(el.content)
      return pandoc.List({pandoc.BlockQuote(blocks)})
    end
  end

  -- ::: {#tab:...} -> preserve id as anchor, pass through content (table + caption)
  -- Extract the caption from the Table AST node and render it as italic text below.
  if id:match("^tab:") then
    local blocks = pandoc.List({
      pandoc.RawBlock("html", '<span id="' .. id .. '"></span>')
    })
    for _, block in ipairs(el.content) do
      if block.t == "Table" then
        -- Extract and clear the caption from the table
        local caption = block.caption and block.caption.long
        if caption and #caption > 0 then
          blocks:insert(block)
          -- Render caption as italicized paragraph below the table
          for _, cap_block in ipairs(caption) do
            if cap_block.t == "Para" or cap_block.t == "Plain" then
              blocks:insert(pandoc.Para(pandoc.List({pandoc.Emph(cap_block.content)})))
            else
              blocks:insert(cap_block)
            end
          end
          -- Clear the caption from the table itself to avoid duplication
          block.caption = {long = pandoc.List({}), short = nil}
        else
          blocks:insert(block)
        end
      else
        blocks:insert(block)
      end
    end
    return blocks
  end

  -- Default: unwrap the div, just return its content
  return el.content
end

-- Fix Pandoc cross-references: [text](#target){reference-type="..." reference="..."}
-- These come through as Link elements with extra attributes.
function Link(el)
  local ref_type = el.attributes["reference-type"]
  if ref_type then
    -- Clean up: remove the Pandoc-specific attributes, keep as plain link
    el.attributes["reference-type"] = nil
    el.attributes["reference"] = nil
  end
  return el
end
