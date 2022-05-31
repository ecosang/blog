---
toc: true
layout: page
title: Research
permalink: /research/
---

- [Timeline](#timeline)
- [Sociotechnical Systems to Enable Smart and Connected Energy-Aware Residential Communities ](#sociotechnical-systems-to-enable-smart-and-connected-energy-aware-residential-communities )
	* [Project Vision](#project-vision)
	* [Field Data Collection](#field-data-collection)
	* [Data-driven Building Energy Normalization](#data-driven-building-energy-normalization)
	* [Online Model for Unit-level Heating and Cooling Energy Predicition](#online-mdoel-for-unit-level-heating-and-cooling-energy-predicition)
	* [Scalable Building Energy Model using Probabilistic Deep learning](#scalable-building-energy-model-using-probabilistic-deep-learning)
- [Liquid desiccant and dew point evaporative cooling based 100% outdoor air system](#liquid-desiccant-and-dew-point-evaporative-cooling-based-100%-outdoor-air-system)
- [Indirect Evaporative Cooler Modeling and Test Chamber Design](#indirect-evaporative-cooler-modeling-and-test-chamber-design)
- [Data Center Cooling](#data-center-cooling)


## Timeline

--- 

![]({{ site.baseurl }}/images/timeline.png "Research timeline")

---

## Sociotechnical Systems to Enable Smart and Connected Energy-Aware Residential Communities 

### Project Vision

![]({{ site.baseurl }}/images/scc_vision.png "Project vision")

- 3-year smart home project with community partners (IHCDA, BWI, Purdue)
- A major student for idea development, figure works, and proposal writing assistance.
- Project management role such as sensor procurement, meeting arrangement, communication between multiple partners/students/faculties.

---

### Field Data Collection

![]({{ site.baseurl }}/images/field_data_collection.png "Field data collection/installation")

- Prototyping and choosing WiFi-based thermostats and circuit-level power sensors and their data collection to a database. 
- Installation and trouble shooting of sensors for 50 residential units located in Indianapolis, IN.
- Documentation of data communication and database schema to work with software developers to accommodate multiple sensors communication in real-time.
- Development of R (Shiny) and HTML based interactive data analytics tool for time-series data (for internal-use).
- Procurement/installation/design of Tablet/Smart speaker for smart home interface (SmartE) with research team.

---

### Data-driven Building Energy Normalization

![]({{ site.baseurl }}/images/normalization.png "Data-driven building energy normalization")

- "A data-driven building energy normalization model for eco-feedback design in smart and connected multi-family residential buildings."
- Energy comparison of residential units in a multi-family residential building as an eco-feedback.
- Normalized groups by considering inter-unit heat transfer and unobserved disturbances.
- Fair comparison of the impact of thermostat behavior on heating/cooling energy consumption.
- Online model update via Bayesian inference to be used for eco-feedback application.
- Conference paper: [PURDUE 2018](https://docs.lib.purdue.edu/ihpbc/319/).

---

### Online Model for Unit-level Heating and Cooling Energy Predicition

![]({{ site.baseurl }}/images/online_model.png "Online model structure")

- "Online building energy model to evaluate heating and cooling-related behavior changes for eco-feedback in a multifamily residential building."
- Unit-level heating and cooling energy prediction model for actionable eco-feedback design a multi-family residential building.
- A single zone gray-box model from thermostat and heat pump power measurement only.
- Online parameter learning with state filtering to be used without a whole year dataset in Bayesian framework.
- Conference paper: [IBPSA 2019](https://par.nsf.gov/servlets/purl/10134059).

---

### Scalable Building Energy Model using Probabilistic Deep learning

![]({{ site.baseurl }}/images/reslstm.png "Scalable model overview")

- "A Scalable Building Modeling Approach using Probabilistic Deep learning (tentative)."
- A household-level heating and cooling energy prediction model using Deep neural network.
- Overcoming the limitation of black-box model through Bayesian update with pre-trained model to be used any types of residential unit.
- Generation of multiple simulated data (EnergyPlus) with stochastic noise (Python EnergyPlus plugin) through Eppy package.
- Solving probabilistic deep learning model by using Pyro and Pytorch.
- In preparation.

---

## Liquid desiccant and dew point evaporative cooling based 100% outdoor air system

![]({{ site.baseurl }}/images/ldeos.png "LDEOS system overview")

- Annual energy simulation for liquid-desiccant and dew point evaporative cooling based 100% outdoor system.
- Implementation of PI controller, empirical liquid desiccant and dew point evaporative cooling model in a BCVTB co-simulation framework with EnergyPlus to test a new control algorithm (variable air volume and temperature control).
- Development of a data-driven empirical model of PEM fuel cell system to be used for LDEOS system as a cogeneration application.
- Conference paper: [ASHRAE 2016](https://www.techstreet.com/standards/st-16-c048-a-variable-volume-and-temperature-vvt-control-strategy-for-a-liquid-desiccant-and-dew-point-evaporative-cooler-assisted-100-outdoor-air-system-ldeos?product_id=1919925).
- Journal papers: [ENB 2016](https://www.sciencedirect.com/science/article/abs/pii/S0378778816300573) [ENB 2015](https://www.sciencedirect.com/science/article/abs/pii/S0378778815302085).

---

## Indirect evaporative cooler modeling and test chamber design

![]({{ site.baseurl }}/images/iec.png "IEC model and test chamber")

- Design of environmental chamber to test the performance of indirect evaporative cooler.
- Installation of sensors and data collection platform on PLC-based SCADA machine including wet-bulb temperature, airflow chamber.
- Design/installation of indirect evaporative cooler with a manufacturing company. 
- A numerical model of indirect evaporative cooler by using finite difference method to design the prototype.
- Journal papers: [ENERGY 2016](https://www.sciencedirect.com/science/article/abs/pii/S0360544216300615), [APEN 2017](https://www.sciencedirect.com/science/article/abs/pii/S030626191730288X)

---

## Data Center Cooling

![]({{ site.baseurl }}/images/data_center.png "Data center cooling experimental site")

- Development various air-side economizers and their annual energy simulation model for data center cooling application.
- Development of a simplified server model that can be used for data center cooling energy simulation.
- Estimating the impact of air containment in a modular data center through one-to-one scale test bed experiment and CFD simulation. 
- Development of excel VBA-based tool to estimate rough annual energy consumption of data center cooling for practical use.
- Journal papers: [APEN 2015](https://www.sciencedirect.com/science/article/abs/pii/S0306261914011167), [ATE 2015](https://www.sciencedirect.com/science/article/abs/pii/S1359431114011508), [ENB 2015](https://www.sciencedirect.com/science/article/abs/pii/S0378778814009049),  [ATE 2016](https://www.sciencedirect.com/science/article/abs/pii/S1359431115005268).
 
