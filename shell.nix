{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  buildInputs = [
    pkgs.python312
    pkgs.python312Packages.pip
    pkgs.python312Packages.requests
    pkgs.python312Packages.flask
    pkgs.python312Packages.python-dotenv
    pkgs.python312Packages.pydub
    pkgs.python312Packages.openai
    pkgs.python312Packages.result
    pkgs.python312Packages.requests
    pkgs.python312Packages.jira
    pkgs.ffmpeg
    pkgs.nodejs
    pkgs.yarn  # Si utilizas yarn para gestionar paquetes de Node.js
  ];
}
