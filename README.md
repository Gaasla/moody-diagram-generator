# Moody Diagram Generator

A Python script that generates high-quality, scalable Moody diagrams in SVG format. The Moody diagram is an essential engineering tool used to determine friction factors for fluid flow in pipes, widely used in fluid mechanics, hydraulic engineering, and HVAC design.

## Features

- **High-Quality SVG Output**: Generates crisp, scalable vector graphics suitable for technical documentation and presentations
- **Complete Moody Diagram**: Includes all essential elements:
  - Reynolds number grid (600 to 100,000,000)
  - Friction factor grid (0.008 to 0.1)
  - Laminar flow region (Hagen-Poiseuille equation)
  - Critical zone highlighting (Re 2000-4000)
  - Transition zone
  - Turbulent flow region with Colebrook curves
  - Smooth pipe curve
  - Relative roughness scale
  - VD scales for air and water at 20°C
- **Professional Styling**: Clean, modern design with proper typography and mathematical symbols
- **Responsive Design**: Auto-scaling elements based on canvas size
- **Engineering Reference Data**: Includes material roughness values, fluid properties, and standard equations

## Generated Output

The script generates a complete Moody diagram as an SVG file with **1400×1000 pixel dimensions** by default. The output includes all essential engineering elements with mathematical accuracy and professional presentation standards.

- **Vector Format**: Infinitely scalable SVG output
- **Print Ready**: Suitable for high-resolution printing
- **Web Friendly**: Lightweight files perfect for web publication
- **Professional Grade**: Publication-quality output for technical documents

**Quick Download**: If you just need a high-quality SVG (under 40KB), you can download it directly from the `output/` directory without running the script.


## Quick Start

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/moody-diagram-generator.git
   cd moody-diagram-generator
   ```

2. **Install dependencies** (requires Python 3.8+):
   ```bash
   pip install numpy
   ```

3. **Generate the diagram**:
   ```bash
   python main.py
   ```

4. **Find your diagram**:
   The SVG file will be saved to `output/moody_diagram.svg`

## Use Cases

- **Engineering Education**: Teaching fluid mechanics and pipe flow concepts
- **Technical Documentation**: Including in reports, manuals, and specifications
- **Design Work**: Reference tool for hydraulic and HVAC system design
- **Research**: Base diagram for fluid flow analysis and presentation
- **Print Media**: High-resolution output suitable for textbooks and technical publications

## Customization

The diagram can be customized through the `config.py` file:
- Canvas dimensions and aspect ratio
- Typography and font sizes
- Grid density and styling

## Contributing

We welcome contributions from the engineering and scientific community! Here's how you can help:

### Ways to Contribute

- **Bug Reports**: Found an issue? Please open a GitHub issue with details
- **Feature Requests**: Suggest new features or improvements
- **Code Contributions**: Submit pull requests for bug fixes or enhancements
- **Documentation**: Help improve documentation and examples
- **Testing**: Test the generator with different parameters and report results
- **Educational Content**: Create tutorials or example use cases

### Ideas for Contributions

- Alternative diagram layouts or styles
- Export formats (PNG, PDF, etc.)
- Interactive features
- Localization for different languages
- Performance optimizations
- Educational annotations and explanations

## Technical Requirements

- Python 3.8 or higher
- NumPy for mathematical calculations
- No external dependencies for core functionality

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Based on the classic Moody diagram developed by Lewis Moody
- Implements standard fluid mechanics equations and correlations

- Technical References:
https://en.wikipedia.org/wiki/Moody_chart

Moody, L. F. (1944), "Friction factors for pipe flow" (PDF), Transactions of the ASME,
66 (8): 671-684, archived (PDF) from the original on 2019-11-26

Rouse, H. (1943). Evaluation of Boundary Roughness.
Proceedings Second Hydraulic Conference, University of Iowa Bulletin 27.

Pigott, R. J. S. (1933). "The Flow of Fluids in Closed Conduits".
Mechanical Engineering. 55: 497-501, 515.

Kemler, E. (1933). "A Study of the Data on the Flow of Fluid in Pipes".
Transactions of the ASME. 55 (Hyd-55-2): 7-32.

Nikuradse, J. (1933). "Strömungsgesetze in Rauen Rohren".
V. D. I. Forschungsheft. 361. Berlin: 1-22. These show in detail the transition
region for pipes with high relative roughness (ε / D > 0.001).

Colebrook, C. F. (1938-1939). "Turbulent Flow in Pipes, With Particular
Reference to the Transition Region Between the Smooth and Rough Pipe Laws".
Journal of the Institution of Civil Engineers. 11 (4).
London, England: 133-156.

## Citation

If you use this tool in academic or professional work, please consider citing:

```
Moody Diagram Generator. (2025). GitHub repository.
https://github.com/TaviTav/moody-diagram-generator
```

---

**Engineering made visual.** Generate professional Moody diagrams for your fluid mechanics projects.