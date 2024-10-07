# rpi-gpio-blinker

A Docker container for testing GPIO access on Raspberry Pi (RPi) by implementing a simple LED blink application using the `gpiozero` library.

## Overview

This project demonstrates how to control an LED connected to a Raspberry Pi's GPIO pins through a Docker container. It serves as a test container for Docker build and push Actions integrated with GPIO access.

## Features

- Simple LED blinking functionality on Raspberry Pi.
- Easily deployable using Docker.
- Integration with GitHub Actions for automated build and publication.

## GitHub Actions

### Docker Publish Workflow

The [`.github/workflows/docker-publish.yml`](.github\workflows\docker-publish.yml) file defines the workflow to build and publish the Docker image whenever changes are pushed. Here are its key components:

- **Triggers**: 
  - The workflow is triggered on pushes to any branches except `main`, as well as on version tags (e.g., `v*`). 
- **Jobs**: 
  - **Build Job**:
    - **Environment Variables**: Sets `REGISTRY` to `ghcr.io` and `IMAGE_NAME` to the repository path.
    - **Checkout**: Uses `actions/checkout@v4` to fetch the repository code.
    - **Install Cosign**: Installs the cosine tool for image signing (except on pull requests).
    - **Set up Buildx**: Configures Docker Buildx for multi-platform image building.
    - **Login**: Authenticates to the Docker registry using `docker/login-action@v3` (also not executed for pull requests).
    - **Extract Metadata**: Generates tags and labels for the Docker image using `docker/metadata-action@v5`.
    - **Build and Push**: Builds and publishes the Docker image using `docker/build-push-action@v5`, caching layer data for faster builds.
    - **Signing Images**: Signs the Docker image using Cosign, ensuring authenticity and integrity.
  
### Release Please Workflow

The [`.github/workflows/release-please.yml`](.github\workflows\realease-please.yml) file automates the release process based on pushes to the `main` branch:

- **Triggers**: 
  - The workflow is activated on pushes to the `main` branch.
- **Jobs**: 
  - **Release Job**:
    - Utilizes the `googleapis/release-please-action@v4` to manage versioning and generate changelogs based on [conventional commit messages](https://www.conventionalcommits.org/en/v1.0.0/).
    - Version bumps follow the semantic versioning scheme (major.minor.patch).
    - Assumes you have a personal access token (PAT) stored as a GitHub secret named `PAT` for API interactions.
    - Pushes a tagged release with the generated changelog
    - Tag triggers the Docker publish workflow to build and publish the updated image.

## Getting Started

### Prerequisites

- A Raspberry Pi with GPIO pins.
- Docker installed on your Raspberry Pi.
- Basic understanding of Python and Docker commands.

### Wiring

To get started, you'll need to connect an LED to your Raspberry Pi. Refer to the following breadboard sketch for the wiring setup:

![breadboard sketch](docs/breadboard_sketch.svg)

Wiring details:
- Connect the longer leg (anode) of the LED to GPIO pin 21.
- Connect the shorter leg (cathode) of the LED to a ground (GND) pin.
- Ensure to use a resistor (e.g., 1kΩ) in series with the LED to prevent current overload.

### Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/FelizCoder/rpi-gpio-blinker.git
    cd rpi-gpio-blinker
    ```
2. Build the Docker image:
    ```bash
    docker build -t rpi-gpio-blinker .
    ```
3. Run the Docker container:
    ```bash
    docker run --device /dev/gpiomem rpi-gpio-blinker
    ```
4. The LED should start blinking on your Raspberry Pi.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Changelog

Please refer to the [CHANGELOG](CHANGELOG.md) for a list of notable changes to this project.

## Additional Information

For more information on `gpiozero`, you can consult the official documentation [here](https://gpiozero.readthedocs.io/en/latest/). For further insights into Docker, visit the [Docker documentation](https://docs.docker.com/).
