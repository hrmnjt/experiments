

## Shell prompt setup - Starship

```console
Documentation:              https://starship.rs/  
Github repository:          https://github.com/starship/starship
```

### Installation for Starship binary

```bash
sh -c "$(curl -fsSL https://starship.rs/install.sh)"
```

### Adding Starship to bashrc

```bash
echo 'eval "$(starship init bash)"' >> ~/.bashrc
```

### Setting up the configuration required

```bash
mkdir -p ~/.config
ln -sf ${PWD}/home/starship.toml ~/.config/starship.toml
```
*Note: run this command from sttp repository root*
