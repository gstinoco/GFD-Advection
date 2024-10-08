# mGFD-Advection
Data and methods for numerically solve Advection Equation using a meshless Generalized Finite Differences Scheme.

All the codes are distributed under MIT License on [GitHub](https://github.com/gstinoco/GFD-Advection) and are free to use, modify, and distribute giving the proper copyright notice.

## Description :memo:
This repository proposes a way to achieve an approximation to Advection Equation in two dimensions for highly irregular regions.

For this, the proposed method uses a Generalized Finite Differences Method for the numerical solution on unstructured clouds of points.

Examples of solving various problems in an irregular region can be found below.

| Titicaca Lake Cloud of Points                                                                        |
| :--------------------------------------------------------------------------------------------------: |
| <img src="Data/Clouds/CUA.png">                                                                      |
|                                                                                                      |
| Example 1                                                                                            |
| <video src="https://github.com/user-attachments/assets/39e1dee8-a36d-431d-b88f-2dbd36975eba">        |
| $\mid\mid e\mid\mid =3.4529379480364844e-05$                                                         |
|                                                                                                      |
| Example                                                                                              |
| <video src="https://github.com/user-attachments/assets/b2bf69c5-3e39-443d-91b4-630a7a2f1dec">        |
| $\mid\mid e\mid\mid = 1.463705206772183e-04$                                                         |
|                                                                                                      |

## Data :open_file_folder:
All the data were taken from Author's [Cloud-Generation Github Repository](https://github.com/gstinoco/Cloud-Generation). The data is free for anyone to use to compare the results using different methods with the same dataset.

The following regions were considered for this repository:
- **BAN**: Banderas bay in Mexico.
- **BLU**: Blue Lagoon in Iceland.
- **CUA**: Unitary square.
- **CUI**: Cuitzeo Lake in Mexico.
- **ENG**: United Kingdom Island.
- **GIB**: Strait of Gibraltar.
- **HAB**: Havana bay.
- **MIC**: Michoacan State in Mexico.
- **PAT**: Patzcuaro Lake in Mexico.
- **TIT**: Titicaca Lake in South America.
- **TOB**: Toba Lake in Indonesia.
- **UCH**: Uchinskoye Reservoir in Russia.
- **VAL**: Valencia Lake in Spain.
- **ZIR**: Zirahuen Lake in Mexico

## How to :microscope:
The codes are self explained and completely documented. Examples on how to perform approximations can be found on the files that approximate the following conditions:
- **Example_1.py**: $$f(x, y, v, a, b, t) = 0.2\exp(\frac{(-(x - c_1 - at)^2 - (y - c_2 - bt)^2)}{0.01}$$

- **Example_2.py**: $$f(x, y, v, a, b, t) = (1 - \frac{(x - c_1 - at)^2 + (y - c_2 - bt)}{0.01}) \exp(\frac{(-(x - c_1 - at)^2 - (y - c_2 - bt)^2)}{0.01}$$

In both examples $c_1$ and $c_2$ represent the $x$ and $y$ coordinates of the center of the region.

These examples can be easily modified to perform approximations with different conditions and coefficients.

## Researchers :scientist:
All the codes presented were developed by:
    
  - **Dr. Gerardo Tinoco Guerrero**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    gerardo.tinoco@umich.mx<br>
    https://orcid.org/0000-0003-3119-770X

  - **Dr. Francisco Javier Domínguez Mota**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    francisco.mota@umich.mx<br>
    https://orcid.org/0000-0001-6837-172X

  - **Dr. José Alberto Guzmán Torres**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    Aula CIMNE-Morelia<br>
    jose.alberto.guzman@umich.mx<br>
    https://orcid.org/0000-0002-9309-9390

  - **Dr. José Gerardo Tinoco Ruiz**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    jose.gerardo.tinoco@umich.mx<br>
    https://orcid.org/0000-0002-0866-4798

## Students :man_student: :woman_student:
  - **Heriberto Arias Rojas**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    heriberto.arias@umich.mx<br>
    https://orcid.org/0000-0002-7641-8310

  - **Gabriela Pedraza Jiménez**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    2220157h@umich.mx<br>
    https://orcid.org/0009-0002-8118-0260
  
  - **Miguel Ángel Rodríguez Velázquez**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    miguel.rodriguez@umich.mx<br>
    https://orcid.org/0009-0009-7245-1517
  
  - **Ricardo Román Gutiérrez**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    ricardo.roman@umich.mx<br>
    https://orcid.org/0000-0001-8521-9391

<!--
  - **Nancy Saray Saucedo León**<br>
    Universidad Michoacana de San Nicolás de Hidalgo<br>
    1153558a@umich.mx<br>
-->
## Funding :dollar:
With the financing of:

  - National Council of Humanities, Sciences and Technologies, CONAHCyT (Consejo Nacional de Humanidades, Ciencias y Tecnologías, CONAHCyT), México.
  
  - Coordination of Scientific Research, CIC-UMSNH (Coordinación de la Investigación Científica de la Universidad Michoacana de San Nicolás de Hidalgo, CIC-UMSNH), México.
  
  - Aula CIMNE-Morelia, México.
