---
type: entity
tags: [react, headless-ui, accessibility, radix-ui, component-library]
sources: ["https://www.radix-ui.com/themes/docs/components/separator"]
updated: 2026-11-20
---

# Radix UI

**Radix UI** is an open-source UI component library designed for building accessible, high-quality design systems and web applications in React. Maintained by WorkOS, it provides unstyled, low-level headless primitives and an official component theme system.

## Architectural Philosophy: Headless Primitives

Unlike traditional opinionated component libraries that bundle pre-configured CSS classes, Radix Primitives focus exclusively on functional mechanics and WAI-ARIA compliance:
- **Zero Default Styles**: No injected CSS or style sheets; developers maintain complete control over styling via Tailwind CSS or custom CSS.
- **WAI-ARIA Accessibility**: Out-of-the-box keyboard navigation, screen reader announcements, focus trapping, and ARIA state attributes.
- **Uncontrolled & Controlled Flexibility**: Primitives support both state modes seamlessly with compound component composition.

## Highlight Primitive: Separator

The `Separator` primitive creates accessible visual and semantic dividers between sections of content:

```tsx
import * as Separator from "@radix-ui/react-separator";

export function Divider({ orientation = "horizontal" }: { orientation?: "horizontal" | "vertical" }) {
  return (
    <Separator.Root
      orientation={orientation}
      className={
        orientation === "horizontal"
          ? "h-px w-full bg-gray-200 my-4"
          : "h-full w-px bg-gray-200 mx-4"
      }
    />
  );
}
```

### Key Features of Separator
- **Orientation Awareness**: Accepts `orientation="horizontal"` or `"vertical"` and automatically updates corresponding `aria-orientation` attributes.
- **Semantic Integrity**: Emits appropriate ARIA roles (`role="separator"` by default, or `role="none"` when marked purely decorative via `decorative={true}`).
- **Composability**: Easily styled using utility tools like `cn()` (see [[react-and-tailwind-ui-patterns]]).

## References
- Related UI Patterns: [[react-and-tailwind-ui-patterns]]
- Official Documentation: [Radix UI Separator](https://www.radix-ui.com/themes/docs/components/separator)
