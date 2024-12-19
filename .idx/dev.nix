{ pkgs, ... }: {
  channel = "stable-24.11";

  packages = [
    (pkgs.python312.withPackages (python-pkgs: with python-pkgs; [
      requests
      flask
      python-dotenv
      pydub
      openai
      jira
      pyopenssl
      cryptography
      bcrypt
      jsonpickle
      pyjwt
      flask-sqlalchemy
      elevenlabs
    ]))
    pkgs.openssh
  ];

  idx = {
    extensions = [
      "ms-python.python"
      "rangav.vscode-thunder-client"
    ];

    workspace = {
      onCreate = {
        # No se usa pip ni venv, todas las dependencias vienen de Nix.
        install = "";
        default.openFiles = [ "README.md" "src/index.html" "main.py" ];
      };
      onStart = {
        run-server = "./devserver.sh";
      };
    };

    previews = {
      enable = true;
      previews = [
        {
          command = [
            "flask"
            "run"
            "--host=0.0.0.0"
            "--port"
            "$PORT"
          ];
          manager = "web";
          id = "flask-app";
        }
      ];
    };
  };
}
