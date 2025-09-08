"""SVG Configuration.

Provides clean, semantic configuration for SVG generation with:
- Intelligent auto-scaling based on canvas dimensions
- Self-adjusting defaults for optimal visual results
"""

import math
from typing import TypedDict, cast

# ======================================================================
# Define classes for type hints
# ======================================================================

class CanvasConfig(TypedDict):
    """Configuration for SVG canvas dimensions and aspect ratio."""

    width: int
    height: int
    preserve_aspect: bool

class TypographyConfig(TypedDict):
    """Configuration for typography and font sizes."""

    font_family: str
    font_family_mono: str
    title: int
    axis_label: int
    axis_tick: int
    small: int
    micro: int

# ======================================================================
# 1. CANVAS & LAYOUT CONFIGURATION
# ======================================================================

CANVAS: CanvasConfig = {
    "width": 1400,  # Total SVG canvas width (px)
    "height": 1000,  # Total SVG canvas height (px)
    "preserve_aspect": True,  # Maintain aspect ratio when scaling
}

# Auto-calculated layout margins based on canvas size
def _calculate_margins(width: int, height: int) -> dict[str, int]:
    """Calculate optimal margins based on canvas dimensions."""
    # Base margins for reference size (1400x1000)
    base_left = max(70, int(width * 0.07))  # ~7% of width, min 70px
    base_right = max(70, int(width * 0.08))  # ~8% of width, min 70px
    base_top = max(120, int(height * 0.11))  # ~11% of height, min 120px
    base_bottom = max(70, int(height * 0.08))  # ~8% of height, min 70px

    return {
        "left": base_left,
        "right": base_right,
        "top": base_top,
        "bottom": base_bottom,
    }

LAYOUT = _calculate_margins(CANVAS["width"], CANVAS["height"])

# =====================================================================
# TYPOGRAPHY (Auto-scaling based on canvas size)
# =====================================================================

def _calculate_font_sizes(width: int, height: int) -> dict[str, int]:
    """Calculate optimal font sizes based on canvas dimensions."""
    # Scale factor based on canvas size relative to reference 1400x1000
    scale = math.sqrt((width * height) / (1400 * 1000))
    scale = max(0.5, min(2.0, scale))  # Clamp between 0.5x and 2.0x

    return {
        "title": max(16, int(24 * scale)),  # Main diagram title
        "axis_label": max(12, int(16 * scale)),
        "axis_tick": max(10, int(13 * scale)),  # Tick labels and annotations
        "small": max(8, int(11 * scale)),  # Small text and details
        "micro": max(7, int(9 * scale)),  # Very small text
    }

font_sizes = _calculate_font_sizes(CANVAS["width"], CANVAS["height"])

TYPOGRAPHY: TypographyConfig = {
    "font_family": "var(--font-family-base, ui-sans-serif, system-ui, sans-serif)",
    "font_family_mono": "var(--font-family-mono, ui-monospace, 'SF Mono', monospace)",
    "title": font_sizes["title"],
    "axis_label": font_sizes["axis_label"],
    "axis_tick": font_sizes["axis_tick"],
    "small": font_sizes["small"],
    "micro": font_sizes["micro"],
}

# =====================================================================
# STYLING SYSTEM (Auto-scaling stroke widths and spacing)
# =====================================================================

def _calculate_stroke_widths(width: int, height: int) -> dict[str, float]:
    """Calculate optimal stroke widths based on canvas dimensions."""
    # Scale factor for stroke widths (less aggressive than font scaling)
    scale = math.sqrt((width * height) / (1400 * 1000))
    scale = max(0.3, min(1.5, scale))  # Clamp between 0.3x and 1.5x

    return {
        "grid_major": max(0.4, 0.8 * scale),
        "grid_minor": max(0.3, 0.5 * scale),
        "frame": max(0.6, 1.0 * scale),
        "curve_default": max(0.5, 1.0 * scale),
        "curve_emphasis": max(0.7, 1.3 * scale),
        "trim_line": max(0.4, 0.9 * scale),
        "marker_stroke": max(0.5, 1.0 * scale),
    }

STYLING = {
    **_calculate_stroke_widths(CANVAS["width"], CANVAS["height"]),
    "opacity_grid_major": 0.45,
    "opacity_grid_minor": 0.25,
    "opacity_critical_zone": 0.10,
    "opacity_trim_line": 0.7,
}

# =====================================================================
# SVG MARKERS & ELEMENTS
# =====================================================================

def _calculate_marker_dimensions(
    width: int, height: int,
) -> dict[str, int | float]:
    """Calculate optimal marker dimensions based on canvas size."""
    scale = math.sqrt((width * height) / (1400 * 1000))
    scale = max(0.5, min(1.5, scale))

    base_size = max(8, int(14 * scale))

    return {
        "arrow_viewbox_size": base_size,
        "arrow_ref_x": base_size,
        "arrow_ref_y": base_size // 2,
        "arrow_marker_width": max(6, int(11 * scale)),
        "arrow_marker_height": max(6, int(11 * scale)),
    }

MARKERS = _calculate_marker_dimensions(CANVAS["width"], CANVAS["height"])

# =====================================================================
# Constants
# =====================================================================

FRICTION_FACTOR_GRID_MAJOR_VALUES = [
    0.008,
    0.009,
    0.010,
    0.012,
    0.014,
    0.016,
    0.018,
    0.020,
    0.025,
    0.030,
    0.035,
    0.040,
    0.045,
    0.050,
    0.055,
    0.060,
    0.070,
    0.080,
    0.090,
    0.100,
]
FRICTION_FACTOR_GRID_MINOR_VALUES = [
    0.0085,
    0.0095,
    0.011,
    0.013,
    0.015,
    0.017,
    0.019,
    0.021,
    0.022,
    0.023,
    0.024,
    0.026,
    0.027,
    0.028,
    0.029,
    0.031,
    0.032,
    0.033,
    0.034,
    0.036,
    0.037,
    0.038,
    0.039,
    0.041,
    0.042,
    0.043,
    0.044,
    0.046,
    0.047,
    0.048,
    0.049,
    0.051,
    0.052,
    0.053,
    0.054,
    0.056,
    0.057,
    0.058,
    0.059,
    0.062,
    0.064,
    0.066,
    0.068,
    0.075,
    0.085,
    0.095,
]

# Tick values for V·D (top scales)
VD_WATER_GRID = [
    0.06,
    0.1,
    0.2,
    0.3,
    0.4,
    0.6,
    0.8,
    1.0,
    2.0,
    4.0,
    6.0,
    8.0,
    10.0,
    20.0,
    40.0,
    60.0,
    100.0,
    200.0,
    400.0,
    600.0,
    1000.0,
    2000.0,
    4000.0,
    6000.0,
    10000.0,
]
VD_AIR_GRID = [
    1.0,
    2.0,
    4.0,
    6.0,
    8.0,
    10.0,
    20.0,
    40.0,
    60.0,
    100.0,
    200.0,
    400.0,
    600.0,
    1000.0,
    2000.0,
    4000.0,
    6000.0,
    10000.0,
    20000.0,
    40000.0,
    60000.0,
    100000.0,
]
ROUGHNESS_GRID_VALUES = [
    1e-5,
    2e-5,
    5e-5,
    1e-4,
    2e-4,
    4e-4,
    5e-4,
    6e-4,
    8e-4,
    0.001,
    0.0015,
    0.002,
    0.003,
    0.004,
    0.005,
    0.006,
    0.008,
    0.01,
    0.0125,
    0.015,
    0.0175,
    0.02,
    0.025,
    0.03,
    0.035,
    0.04,
    0.045,
    0.05,
    0.06,
    0.07,
]

RE_MIN: float = 6e2  # 600 - minimum Reynolds number
RE_MAX: float = 1e8  # 100,000,000 - maximum Reynolds number
FRICTION_FACTOR_MIN: float = 8e-3  # 0.008
FRICTION_FACTOR_MAX: float = 1e-1  # 0.1
CRITICAL_ZONE_START: float = 2000
CRITICAL_ZONE_END: float = 4000
RELATIVE_ROUGHNESS_MIN: float = 1e-5  # 0.00001
RELATIVE_ROUGHNESS_MAX: float = 1e-1  # 0.1

INFO_MATERIAL = {
    "Material": "\u03B5 (mm)",
    "Riveted steel": "0.9 - 9",
    "Concrete": "0.3 - 3",
    "Wood stave": "0.18 - 0.9",
    "Cast iron": "0.25",
    "Galvanized iron": "0.15",
    "Asphalted cast iron": "0.12",
    "Commercial steel": "0.046",
    "Drawn tubing": "0.0015",
}

INFO_FLUID = {
    "Fluid at 20°C": "\u03bd (m²/s)",
    "Water": "1.003e-006",
    "Air (101.325 kPa)": "1.511e-005",
}

INFO_LATITUDE = {
    "Latitude (WGS84)": "g (m/s²)",
    "0.00° Sea Level": "9.78033",
    "45.5° Standard": "9.80665",
    "90° Sea Level": "9.83219",
}

INFO_EQUATION = [
    "Smooth pipes, r = 0",
    "1/\u221af = 2 log(R \u221af) - 0.8",
    " ",
    "Hagen-Poiseuille equation",
    "R \u2264 2300,  f = 64/R",
    " ",
    "Colebrook equation, (R \u2265 2300)",
    "1/\u221af = -2 log(r/3.7 + 2.51/(R \u221af))",
    " ",
    "Continuity equation Q = A V",
    "A = \u03c0 D\u00b2/4, V = 4Q(\u03c0 D\u00b2)",
]

# =====================================================================
# EXPORT CONFIGURATION
# =====================================================================

# Type definitions for configuration
class SVGConfigDict(TypedDict):
    """TypedDict defining the structure and types for SVG configuration.

    Contains all settings related to the diagram including dimensions,
    typography, styling, markers, and various constants used for
    rendering the Moody diagram.
    """

    # Canvas settings
    width: int
    height: int
    preserve_aspect: bool
    # Layout settings
    left: int
    right: int
    top: int
    bottom: int
    # Typography settings
    font_family: str
    font_family_mono: str
    title: int
    axis_label: int
    axis_tick: int
    small: int
    micro: int
    # Styling settings
    grid_major: float
    grid_minor: float
    frame: float
    curve_default: float
    curve_emphasis: float
    trim_line: float
    marker_stroke: float
    opacity_grid_major: float
    opacity_grid_minor: float
    opacity_critical_zone: float
    opacity_trim_line: float
    # Markers
    arrow_viewbox_size: int
    arrow_ref_x: int
    arrow_ref_y: int
    arrow_marker_width: int
    arrow_marker_height: int
    # Grid values and constants
    FRICTION_FACTOR_GRID_MAJOR_VALUES: list[float]
    FRICTION_FACTOR_GRID_MINOR_VALUES: list[float]
    VD_AIR_GRID: list[float]
    VD_WATER_GRID: list[float]
    NU_WATER: float
    NU_AIR: float
    ROUGHNESS_GRID_VALUES: list[float]
    RE_MIN: float
    RE_MAX: float
    FRICTION_FACTOR_MIN: float
    FRICTION_FACTOR_MAX: float
    CRITICAL_ZONE_START: float
    CRITICAL_ZONE_END: float
    RELATIVE_ROUGHNESS_MIN: float
    RELATIVE_ROUGHNESS_MAX: float
    INFO_MATERIAL: dict[str, str]
    INFO_FLUID: dict[str, str]
    INFO_LATITUDE: dict[str, str]
    INFO_EQUATION: list[str]

SVG_CONFIG = cast("SVGConfigDict", {
    **CANVAS,
    **LAYOUT,
    **TYPOGRAPHY,
    **STYLING,
    **MARKERS,
    "FRICTION_FACTOR_GRID_MAJOR_VALUES": FRICTION_FACTOR_GRID_MAJOR_VALUES,
    "FRICTION_FACTOR_GRID_MINOR_VALUES": FRICTION_FACTOR_GRID_MINOR_VALUES,
    "VD_AIR_GRID": VD_AIR_GRID,
    "VD_WATER_GRID": VD_WATER_GRID,
    "NU_WATER": 1.003e-6,  # m²/s @ 20°C
    "NU_AIR": 1.511e-5,  # m²/s @ 20°C
    "ROUGHNESS_GRID_VALUES": ROUGHNESS_GRID_VALUES,
    "RE_MIN": RE_MIN,
    "RE_MAX": RE_MAX,
    "FRICTION_FACTOR_MIN": FRICTION_FACTOR_MIN,
    "FRICTION_FACTOR_MAX": FRICTION_FACTOR_MAX,
    "CRITICAL_ZONE_START": CRITICAL_ZONE_START,
    "CRITICAL_ZONE_END": CRITICAL_ZONE_END,
    "RELATIVE_ROUGHNESS_MIN": RELATIVE_ROUGHNESS_MIN,
    "RELATIVE_ROUGHNESS_MAX": RELATIVE_ROUGHNESS_MAX,
    "INFO_MATERIAL": INFO_MATERIAL,
    "INFO_FLUID": INFO_FLUID,
    "INFO_LATITUDE": INFO_LATITUDE,
    "INFO_EQUATION": INFO_EQUATION,
})

