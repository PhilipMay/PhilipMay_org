# NixOS

## Links

- [NixOS Manual (stable)](https://nixos.org/manual/nixos/stable/)
  - [User Management](https://nixos.org/manual/nixos/stable/index.html#sec-user-management)
- [NixOS Wiki](https://nixos.wiki/wiki/Main_Page)
  - [SSH public key authentication](https://nixos.wiki/wiki/SSH_public_key_authentication)
- [Nixpkgs Manual](https://nixos.org/manual/nixpkgs/stable/)
- [Nix Reference Manual](https://nixos.org/manual/nix/stable/)
  - [Main Commands](https://nixos.org/manual/nix/stable/command-ref/main-commands#main-commands)
- [Releases](https://nixos.org/manual/nixos/stable/release-notes)
- Searches
  - Packages: <https://search.nixos.org/packages>
  - Options: <https://search.nixos.org/options>
  - Flakes: <https://search.nixos.org/flakes>
- Community
  - [Matrix Chat](https://matrix.to/#/#community:nixos.org)

## Packages

- Docker: https://nixos.wiki/wiki/Docker
- Tor: https://nixos.wiki/wiki/Tor

## Know-how

- get path to nix repository: `nix-instantiate --eval -E '<nixpkgs>'` - also see [Nix Search Paths](https://nixos.org/guides/nix-pills/nix-search-paths.html)
- list available profiles: `nix-env --list-generations --profile /nix/var/nix/profiles/system`
- update the system: `nixos-rebuild switch --upgrade`

## Cleanup

- delete generations from the current profile
  - delete all except current: `nix-env --delete-generations old`
  - delete generations more than 14 days ago: `nix-env --delete-generations 14d`
  - keep last 2 generations, along with any newer than current: `nix-env --delete-generations +2`
- after removing old generations run garbage collector: `nix-store --gc`
- delete unreachable store objects: `nix-collect-garbage -d`
- also see: <https://nixos.org/manual/nix/stable/package-management/garbage-collection>

## Installation

- [Installing from another Linux distribution](https://nixos.org/manual/nixos/stable/#sec-installing-from-other-distro)

## ZFS

- https://nixos.wiki/wiki/ZFS
  - https://openzfs.github.io/openzfs-docs/Getting%20Started/NixOS/index.html
- https://nixos.org/manual/nixos/stable/index.html#sec-linux-zfs
