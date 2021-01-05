# spack-repos

Spack repos for HPC&DE, USTB.

Packages in this repo were set up for HPC&DE and tested with a limited releases of Spack (mostly with v0.16).

## Namespaces

- hpcde

## Usage

Step 1: clone this repository to wherever you want.

Step 2: add path `hpcde/` to your Spack repo configuration `repos.yaml`.

```bash
# edit the configuration
$ spack config edit repos

repos:
  - /path/to/spack-repos/hpcde
```

Step 3: make sure these packages could be found by Spack.

```bash
$ spack repo list
```

