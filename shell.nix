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
        result
        requests
        # HTTPS
        pyopenssl
        cryptography
        # Cifrado en la base de datos
        bcrypt
        jsonpickle
    ]))
  ];
}
