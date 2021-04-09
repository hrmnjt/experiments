# Dotfiles

## Shell prompt setup - Starship.rs

```bash
mkdir -p ~/.config
ln -sf ${PWD}/usr/starship.toml ~/.config/starship.toml
```
*Note: run this command from sttp repository root*


<details>
<summary>About starship.rs</summary>

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
</details>



## Bash `profile` and `bashrc` setup

```bash
ln -sf ${PWD}/usr/.profile ~/.profile
ln -sf ${PWD}/usr/.bashrc ~/.bashrc
```
*Note: run this command from sttp repository root*
