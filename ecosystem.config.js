module.exports = {
  apps: [{
    name: "palopoli-backend",
    script: "./backend/index.js",
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: "development",
      PORT: 3333
    },
    env_production: {
      NODE_ENV: "production",
      PORT: 3333
    }
  }],

  deploy: {
    production: {
      user: 'seu_usuario',
      host: 'seu_servidor',
      ref: 'origin/main',
      repo: 'git@github.com:Winove33win/palopoli-adv-nexus.git',
      path: '/var/www/palopoli-adv-nexus',
      'post-deploy': 'npm install && pm2 reload ecosystem.config.js --env production'
    }
  }
};
