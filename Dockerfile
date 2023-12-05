# Start from the Jupyter SciPy Notebook image
FROM jupyter/scipy-notebook

# Install additional packages that are not included in the base image
RUN conda install --quiet --yes \
    'ipympl' \
    'nodejs' \
    && conda clean --all -f -y
