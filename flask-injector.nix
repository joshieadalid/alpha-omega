# toolz.nix
{ lib
, buildPythonPackage
, fetchPypi
, setuptools
, wheel
}:

with import <nixpkgs> {};
#with pkgs.python312Packages;

buildPythonPackage rec {
  pname = "flask-injector";
  version = "0.15.0";
  format = "wheel";
  src = python312Packages.fetchPypi rec {
    inherit pname version format;
    sha256 = "9908904ab8d8830e5160b274fd5dd73453741c9c618d3fc6deb2b08d894f4ece";
    dist = python;
    python = "py3";
  };
  propagatedBuildInputs = [
    python312Packages.flask
    python312Packages.injector
    ];
}