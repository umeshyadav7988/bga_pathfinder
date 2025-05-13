# BGA Pathfinder

## Overview

The BGA Pathfinder is a project that implements the A* pathfinding algorithm to assist with Ball Grid Array (BGA) breakout routing. The algorithm is designed to find optimal paths across multi-layer grids, ensuring efficient routing of traces for BGA designs. The project also visualizes the pathfinding process using matplotlib.

This repository contains the full code for the pathfinding logic, along with the necessary dependencies to run the project. It's a useful tool for engineers and developers working with BGA designs or similar routing problems.

## Features

- **A* Pathfinding Algorithm**: Implements a popular and efficient pathfinding algorithm to find the shortest path between two points on a grid.
- **Multi-Layer Support**: Handles multi-layer traces commonly used in BGA designs.
- **Visualization**: Uses `matplotlib` to visualize the pathfinding process and the grid layout.
- **Customizable**: The code is easily modifiable to fit specific routing or design needs.

## Screenshot

Here’s a screenshot of the pathfinding visualization:

![Figure_1](https://github.com/user-attachments/assets/b8cbf276-a3bb-4fbf-be9c-50f4bb4f886b)



## Installation

To get started with the BGA Pathfinder project, follow these steps:

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/umeshyadav7988/bga_pathfinder.git
````

Then, navigate to the project directory:

```bash
cd bga_pathfinder
```

### 2. Install Dependencies

Install the required Python dependencies using pip:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries, including `matplotlib` for visualization and other dependencies needed for pathfinding.

### 3. Run the Project

To run the project, execute the following command:

```bash
python main.py
```

This will start the pathfinding logic, and the program will output a visual representation of the pathfinding process using `matplotlib`.

## Usage

* **Grid Setup**: The grid for pathfinding can be customized. You can define obstacles and empty spaces on the grid to suit your requirements.
* **Start/End Points**: Define your start and end points for the A\* algorithm to compute the shortest path.
* **Multi-Layer Routing**: The project supports multi-layer routing, making it suitable for BGA designs.
* **Path Visualization**: The resulting paths are visualized in a grid, helping you to easily understand the pathfinding process.

## Contributing

Contributions to the BGA Pathfinder project are welcome! If you have suggestions for improvements or would like to add new features, feel free to submit a pull request. Please make sure to follow the guidelines below:

1. Fork the repository.
2. Create a new branch for your changes.
3. Make the necessary modifications and add tests if applicable.
4. Submit a pull request with a detailed description of your changes.

## Contact

If you have any questions or need support, feel free to reach out:

* **Email**: [umeshyadav7988@gmail.com](mailto:umeshyadav7988@gmail.com)
* **GitHub Repository**: [https://github.com/umeshyadav7988/bga\_pathfinder](https://github.com/umeshyadav7988/bga_pathfinder)

Thank you for using the BGA Pathfinder project! 
