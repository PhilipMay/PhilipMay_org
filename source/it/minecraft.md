# Minecraft

## Links

- Paper MC: https://docs.papermc.io/paper/admin
- LuckPerms: <https://luckperms.net/wiki/Usage>
- EssentialsX: <https://essentialsx.net/wiki/Home.html>
  - Commands: <https://essinfo.xeya.me/commands.html>
  - Permissions: <https://essinfo.xeya.me/permissions.html>

## Permissions

- list all groups: `lp listgroups`
- give permission to user: `lp user <username> permission set <permission_name> true`
- list permissions of a user: `lp user <username> permission info`
- also see LuckPerms: <https://luckperms.net/wiki/Usage>

## Docker

- marctv/minecraft-papermc-server
  - https://hub.docker.com/r/marctv/minecraft-papermc-server
  - https://github.com/mtoensing/Docker-Minecraft-PaperMC-Server
- connect to console: `docker attach <container_name>`
- disconnect from console: `ctrl + p` + `ctrl + q`

## Commands
- whitelisting
  - activate whitelist: `/whitelist on`
  - add player to whitelist: `/whitelist add <player>`
- keep inventory: `/gamerule keepInventory true`
- give item: `/give <player> <item_name> [amount]`
- switch game mode: `/gamemode creative`
- prevent Creepers from destroying blocks: `/gamerule mobGriefing false`
