{ pkgs ? import <nixpkgs> {} }:

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
        # Cifrado en la base de datos
        bcrypt
        jsonpickle
        # Flask
        pyjwt
        # Base de datos
        flask-sqlalchemy
        # TTS
        elevenlabs
    ]))
  ];
}
