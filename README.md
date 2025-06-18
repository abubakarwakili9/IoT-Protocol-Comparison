# IoT Protocol Comparison: LwM2M vs Matter

## 🎯 Project Overview
Comprehensive comparison of LwM2M and Matter protocols using real hardware implementation and OSI layer analysis.

## 🛠️ Hardware
- Raspberry Pi Pico W (RP2350)
- WiFi Network Infrastructure

## 📊 Key Results
- LwM2M: 30-45% more bandwidth efficient
- Matter: Better for rich device interactions
- Binary encoding: 25% size reduction vs JSON

## 🚀 Quick Start
1. Set up Leshan server: `java -jar leshan-server-demo.jar`
2. Upload Arduino clients to Pico W
3. Run analysis: `python osi_layer_analyzer.py`

## 📁 Project Structure
- `lwm2m-project/`: LwM2M implementation
- `matter-project/`: Matter implementation  
- `data-analysis/`: Analysis tools and results
- `docs/`: Documentation and reports

## 📈 Results
See `data-analysis/results/` for:
- Message size comparisons
- OSI layer overhead analysis
- Protocol efficiency metrics
- Research visualizations

## 🎓 Academic Use
This project implements real IoT protocols for research purposes. 
Results suitable for academic publication.

## 📄 License
MIT License - See LICENSE file for details
