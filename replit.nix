{ pkgs }: {
    deps = [
        pkgs.neofetch
        pkgs.python39Packages.pip
        pkgs.qtile
        pkgs.cowsay
    ];
}