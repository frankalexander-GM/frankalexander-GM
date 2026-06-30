<div align="center">

<!-- Pacman Animation SVG -->
<svg width="600" height="200" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="neonGlow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00d4ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0088ff;stop-opacity:1" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <filter id="textGlow">
      <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
    <radialGradient id="pacmanBody" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#ffee00" />
      <stop offset="100%" style="stop-color:#ffaa00" />
    </radialGradient>
  </defs>

  <!-- Dots -->
  <circle cx="100" cy="100" r="6" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="0.8s" repeatCount="indefinite" begin="0s"/>
  </circle>
  <circle cx="140" cy="100" r="6" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="0.8s" repeatCount="indefinite" begin="0.1s"/>
  </circle>
  <circle cx="180" cy="100" r="6" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="0.8s" repeatCount="indefinite" begin="0.2s"/>
  </circle>
  <circle cx="220" cy="100" r="6" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="0.8s" repeatCount="indefinite" begin="0.3s"/>
  </circle>
  <circle cx="260" cy="100" r="6" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="0.8s" repeatCount="indefinite" begin="0.4s"/>
  </circle>
  <circle cx="300" cy="100" r="6" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="0.8s" repeatCount="indefinite" begin="0.5s"/>
  </circle>
  <circle cx="340" cy="100" r="6" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="0.8s" repeatCount="indefinite" begin="0.6s"/>
  </circle>
  <circle cx="380" cy="100" r="6" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="opacity" values="0.3;1;0.3" dur="0.8s" repeatCount="indefinite" begin="0.7s"/>
  </circle>

  <!-- Special big dot -->
  <circle cx="460" cy="100" r="10" fill="#00d4ff" filter="url(#glow)">
    <animate attributeName="r" values="10;14;10" dur="1s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;1;0.5" dur="1s" repeatCount="indefinite"/>
  </circle>

  <!-- Pacman moving -->
  <g>
    <animateTransform attributeName="transform" type="translate" values="-40,0;520,0" dur="5s" repeatCount="indefinite"/>
    <g filter="url(#glow)">
      <!-- Pacman body - changes mouth angle -->
      <path d="M 0,100 A 25,25 0 1,1 50,100 L 42,100 A 17,17 0 1,0 8,100 Z" fill="url(#pacmanBody)">
        <animate attributeName="d" 
          values="M 0,100 A 25,25 0 1,1 50,100 L 42,100 A 17,17 0 1,0 8,100 Z;
                  M 0,100 A 25,25 0 1,1 50,100 L 50,95 L 50,105 Z;
                  M 0,100 A 25,25 0 1,1 50,100 L 42,100 A 17,17 0 1,0 8,100 Z"
          dur="0.3s" repeatCount="indefinite"/>
      </path>
      <!-- Pacman eye -->
      <circle cx="13" cy="90" r="3" fill="#111">
        <animate attributeName="cx" values="13;15;13" dur="0.3s" repeatCount="indefinite"/>
      </circle>
    </g>
  </g>

  <!-- Ghost -->
  <g>
    <animateTransform attributeName="transform" type="translate" values="520,0;-60,0" dur="6s" repeatCount="indefinite"/>
    <g filter="url(#glow)">
      <path d="M 10,100 L 10,120 C 10,125 15,125 17,120 L 20,115 L 23,120 C 25,125 30,125 30,120 L 30,100 Z" fill="#ff4466"/>
      <rect x="10" y="88" width="20" height="12" rx="10" fill="#ff4466"/>
      <!-- Eyes -->
      <circle cx="15" cy="93" r="3" fill="white"/>
      <circle cx="25" cy="93" r="3" fill="white"/>
      <circle cx="16" cy="93" r="1.5" fill="#111"/>
      <circle cx="26" cy="93" r="1.5" fill="#111"/>
      <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
    </g>
  </g>

  <!-- Neon line decoration -->
  <line x1="50" y1="150" x2="550" y2="150" stroke="#00d4ff" stroke-width="1" opacity="0.3" filter="url(#glow)">
    <animate attributeName="opacity" values="0.1;0.5;0.1" dur="3s" repeatCount="indefinite"/>
  </line>
</svg>

<br>

<!-- Typing SVG -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=500&color=00D4FF&center=true&vCenter=true&repeat=true&width=500&height=60&lines=Hey%2C+I'm+Frank+Alexander!;%F0%9F%87%A8%F0%9F%87%B4+Colombia;%F0%9F%92%BB+Full+Stack+Developer;%F0%9F%8E%AE+Gamer+%26+Tech+Enthusiast;%F0%9F%9A%80+Building+RiftZone" alt="typing" />

<br>

<!-- Skills -->
<img src="https://skillicons.dev/icons?i=java,python,js,ts,html,css,react,nextjs,flask,bootstrap,tailwind,prisma,postgres,mysql,sqlite,git,docker,linux,eclipse,vscode&theme=dark&perline=10" />

<br><br>

<!-- Social badges -->
<a href="https://discord.gg/C23PcduvTp"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" /></a>
<a href="mailto:riftzone.oficial@gmail.com"><img src="https://img.shields.io/badge/Gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white" /></a>
<a href="https://github.com/frankalexander-GM"><img src="https://img.shields.io/badge/GitHub-00D4FF?style=for-the-badge&logo=github&logoColor=black" /></a>

<br><br>

<!-- RiftZone Section -->
<h2>🎮 <a href="https://riftzone.online" style="color:#00d4ff;text-decoration:none;">RiftZone</a> 🎮</h2>
<p><i>The ultimate gaming social network</i></p>
<br>

<!-- Stats Graph -->
<img src="https://github-readme-activity-graph.vercel.app/graph?username=frankalexander-GM&bg_color=0a0a0a&color=00d4ff&line=0088ff&point=00d4ff&area=true&hide_border=true&radius=8" width="95%"/>

<br><br>

<!-- Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0A0A0A,100:00D4FF&height=120&section=footer&text=Code%20by%20day%2C%20game%20by%20night%20%E2%98%80%EF%B8%8F&fontSize=18&fontColor=00d4ff&animation=fadeIn" width="100%" />

</div>
