{ pkgs ? import <nixpkgs> {} }:
let
  flask-injector = pkgs.python312Packages.buildPythonPackage rec {
    pname = "flask-injector";
    version = "0.15.0";
    format = "wheel";
    src = pkgs.fetchurl {
      url = "https://files.pythonhosted.org/packages/44/a0/e7964d1d1b8fb64c62988de6a20ee06573354e0a0d9653b6e659323920e9/Flask_Injector-0.15.0-py2.py3-none-any.whl";
      sha256 = "9908904ab8d8830e5160b274fd5dd73453741c9c618d3fc6deb2b08d894f4ece";

    };

    propagatedBuildInputs = with pkgs.python312Packages; [ flask injector ];
  };
in
pkgs.mkShell {
  buildInputs = [
    (pkgs.python312.withPackages (python-pkgs: with python-pkgs; [
        requests
        flask
        python-dotenv
        pydub
        # APIs
        openai
        jira
        requests
        # HTTPS
        pyopenssl
        cryptography
        jsonpickle

        # Cifrado en la base de datos
        bcrypt
        pyjwt
        # Flask
        flask-injector
        # Base de datos (minutas)
        flask-sqlalchemy
        flask-migrate # al cambiar esquemas
        # Text-to-speech
        elevenlabs
        # Reportes
        weasyprint

        # login-server
        flask-bcrypt
        flask-cors
    ]))
    pkgs.nodejs
  ];
}
