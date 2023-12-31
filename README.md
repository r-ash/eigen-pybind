# eigen-pybind

Install Eigen on your computer, on Ubuntu easiest way for me was to install `libeigen3-dev`

```
sudo apt-get install libeigen3-dev
```

This uses hatch to install python dependencies. CMake needs these to findable, set the virtual environment directory to install the python packages into using the hatch config at `~/.config/hatch/config.toml`
And set this section

```
[dirs.env]
virtual = ".direnv"
```

Then install the python dependencies with hatch and build with CMake

```
hatch shell
cmake -S . -B build
cmake --build build
```

Then to test it

```
cd build
python3
```

```python
import example
example.add(1, 2)
```

To run test functions

```
./scripts/test
```

As far as I can see the Eigen::Tensor bindings in pybind11 are not well 
documented. A lot of this was based off reading https://github.com/pybind/pybind11/pull/4201/files

## License

`eigen-pybind` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
