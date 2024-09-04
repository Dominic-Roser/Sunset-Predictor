# Homebrew

Package manager installation used with node.js 

https://brew.sh/


# Node.js

## Windows

```
# installs fnm (Fast Node Manager)
winget install Schniz.fnm

# download and install Node.js
fnm use --install-if-missing 20

# verifies the right Node.js version is in the environment
node -v # should print `v20.15.1`

# verifies the right NPM version is in the environment
npm -v # should print `10.7.0`
```

## Mac 
```
# NOTE:
# Homebrew is not a Node.js package manager. Please ensure it is already installed
# on your system. Follow official instructions at https://brew.sh/
# Homebrew only supports installing major Node.js versions and might not support
# the latest Node.js version from the 20 release line.

# download and install Node.js
brew install node@20

# verifies the right Node.js version is in the environment
node -v # should print `v20.15.1`

# verifies the right NPM version is in the environment
npm -v # should print `10.7.0`
```

