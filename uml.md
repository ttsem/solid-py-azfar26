# UML Diagram

For the Icon class in `Debts.py` file.

```txt
              ┌─────────────────────────┐
              │     Icon (abstract)     │
              ├─────────────────────────┤
              │ - speed: float          │
              │ - glow: float           │
              │ - energy: float         │
              │ - x: int                │
              │ - y: int                │
              ├─────────────────────────┤
              │ + move(): void          │
              │ + flair(): void         │
              └───────────▲─────────────┘
                          │
     ┌────────────────────┼────────────────────┐
     │                    │                    │
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│   Spinner     │   │   Slider      │   │   Hopper      │
├───────────────┤   ├───────────────┤   ├───────────────┤
│ - clockwise: bool │ - vertical: bool  │ - visible: bool │
│ - expand: bool    │ - distance: int   │ - xcoord: int   │
│                   │                   │ - ycoord: int   │
├───────────────┤   ├───────────────┤   ├───────────────┤
│ + spin(): void │   │ + slide(): void │   │ + hop(): void │
│ + move(): void │   │ + move(): void  │   │ + move(): void│
│ + flair(): void│   │ + flair(): void │   │ + flair():void│
└───────────────┘   └───────────────┘   └───────────────┘
```
