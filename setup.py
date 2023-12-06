from setuptools import setup

setup(
    name='mplheatmap',
    version='0.1.0',
    author='Frederic Schell',
    author_email='frederic.schell@iws.fraunhofer.de',
    
    description='Convenience utility to create interpolated 2d heatmaps',
    py_modules=['mplheatmap'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License'
    ],
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy'
    ],
    python_requires='>=3.6'
)
