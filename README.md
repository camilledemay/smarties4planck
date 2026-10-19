# Smarties4Planck

Efficient simulation of beam-convolved Planck maps from arbitrary input skies.

Smarties4Planck is a high-level wrapper around the
[Smarties](https://github.com/simonsobs/smarties) package. It reads Planck beams
and polmoments (aka h-maps), converts them into the format and conventions used
by Smarties, and calls Smarties to perform the beam convolution.

The underlying formalism is described in [Demay et al., 2026]() and
[Morshed et al., in prep.](). For practical usage you can refer to the
[example notebook](example_notebook.ipynb).

## Inputs

The code takes the following inputs:

- `alms`, spherical harmonic coefficients of the input sky.
- `blms`, Planck beam harmonic coefficients.
- Planck polmoments.

The polmoments and `blms` are available at NERSC:

- `blms`: `/global/cfs/cdirs/cmb/data/planck2020/npipe/aux/beams`
- polmoments: `/global/cfs/cdirs/cmb/data/planck2020/npipe/aux/polmoments`

## Installation

To install this package with uv, run

```bash
uv add "smarties4planck @ git+https://github.com/camilledemay/smarties4planck"
```
Alternatively clone this repository and run
```bash
pip install path\to\repo\dir
``` 
> **Note:** `pip` does not read `uv.lock`. If you install with `pip`, pin
> Smarties to the commit recorded in `uv.lock` (under the `[[package]]` entry
> for `smarties`, in the `source = { git = ... ?rev=<sha> ... }` field) rather
> than letting it resolve `@main`, e.g.
> `pip install --force-reinstall "smarties @ git+https://github.com/simonsobs/smarties@<sha>"`.
> This ensures you get the same Smarties version the project was tested against


This code relies on [ducc0](https://gitlab.mpcdf.mpg.de/mtr/ducc) to compute harmonic transforms. As detailed in ducc0 documentation, for best performance it is recommended to compile it from source.
