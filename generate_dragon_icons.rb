#!/usr/bin/env ruby
# ==============================================================================
#  KALI DRAGON SUITE - CYBERPUNK NEON GLOW ICON ENGINE (RUBY 3.3)
# 100% Comprehensive Universal Master Edition (Zero Fallbacks)
# ==============================================================================

require 'fileutils'

BASE_DIR = File.expand_path(__dir__)
VARIANTS_DIR = File.join(BASE_DIR, "variants")

COLORS = {
  "red"     => { name: "Red",     neon: "#ff0000", dim: "#ec0000", inherit: "Flat-Remix-Red-Dark" },
  "blue"    => { name: "Blue",    neon: "#00b0ff", dim: "#2979ff", inherit: "Flat-Remix-Blue-Dark" },
  "green"   => { name: "Green",   neon: "#00e676", dim: "#00c853", inherit: "Flat-Remix-Green-Dark" },
  "yellow"  => { name: "Yellow",  neon: "#ffd600", dim: "#ffc107", inherit: "Flat-Remix-Yellow-Dark" },
  "purple"  => { name: "Purple",  neon: "#d500f9", dim: "#aa00ff", inherit: "Flat-Remix-Purple-Dark" },
  "orange"  => { name: "Orange",  neon: "#ff6d00", dim: "#ff5722", inherit: "Flat-Remix-Orange-Dark" },
  "lime"    => { name: "Lime",    neon: "#76ff03", dim: "#64dd17", inherit: "Flat-Remix-Green-Dark" },
  "pink"    => { name: "Pink",    neon: "#ff4081", dim: "#f50057", inherit: "Flat-Remix-Pink-Dark" },
  "cyan"    => { name: "Cyan",    neon: "#18ffff", dim: "#00e5ff", inherit: "Flat-Remix-Teal-Dark" },
  "teal"    => { name: "Teal",    neon: "#00f2fe", dim: "#00b4d8", inherit: "Flat-Remix-Teal-Dark" },
  "gold"    => { name: "Gold",    neon: "#ffab00", dim: "#ffd700", inherit: "Flat-Remix-Yellow-Dark" },
  "indigo"  => { name: "Indigo",  neon: "#536dfe", dim: "#3d5afe", inherit: "Flat-Remix-Blue-Dark" },
  "mint"    => { name: "Mint",    neon: "#64ffda", dim: "#00bfa5", inherit: "Flat-Remix-Teal-Dark" },
  "ruby"    => { name: "Ruby",    neon: "#e91e63", dim: "#c2185b", inherit: "Flat-Remix-Red-Dark" },
  "magenta" => { name: "Magenta", neon: "#ff007f", dim: "#e00070", inherit: "Flat-Remix-Pink-Dark" }
}

class GeminiWireframeFactory
  # ----------------------------------------------------------------------------
  # 1. BLUEPRINT DOCUMENT WITH NEON GLOW
  # ----------------------------------------------------------------------------
  def self.build_doc(c_neon, c_dim, label_text, glyph_svg)
    <<~SVG
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
        <defs>
          <filter id="neon-glow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="2.2" result="blur1"/>
            <feGaussianBlur stdDeviation="4.5" result="blur2"/>
            <feMerge>
              <feMergeNode in="blur2"/>
              <feMergeNode in="blur1"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>

        <!-- Ambient Glow Halo behind document -->
        <path d="M 26,8 L 62,8 L 78,24 L 78,88 Q 78,92 74,92 L 26,92 Q 22,92 22,88 L 22,12 Q 22,8 26,8 Z" 
              fill="none" stroke="#{c_neon}" stroke-width="5" opacity="0.35" filter="url(#neon-glow)"/>

        <!-- Solid Dark Base Plate (#16191f) -->
        <path d="M 26,8 L 62,8 L 78,24 L 78,88 Q 78,92 74,92 L 26,92 Q 22,92 22,88 L 22,12 Q 22,8 26,8 Z" fill="#16191f"/>

        <!-- Outer Double Wireframe Outline with Glow Core -->
        <path d="M 26,8 L 62,8 L 78,24 L 78,88 Q 78,92 74,92 L 26,92 Q 22,92 22,88 L 22,12 Q 22,8 26,8 Z" 
              fill="none" stroke="#{c_neon}" stroke-width="2.6" opacity="0.4"/>
        <path d="M 26,8 L 62,8 L 78,24 L 78,88 Q 78,92 74,92 L 26,92 Q 22,92 22,88 L 22,12 Q 22,8 26,8 Z" 
              fill="none" stroke="#{c_neon}" stroke-width="1.6" stroke-linejoin="round"/>
        <path d="M 27,10 L 61,10 L 76,25 L 76,86 Q 76,90 72,90 L 27,90 Q 24,90 24,87 L 24,13 Q 24,10 27,10 Z" 
              fill="none" stroke="#{c_dim}" stroke-width="0.7" stroke-linejoin="round" opacity="0.7"/>

        <!-- Spine Left Margin Line -->
        <line x1="26" y1="9" x2="26" y2="91" stroke="#{c_neon}" stroke-width="2.2" opacity="0.4"/>
        <line x1="26" y1="9" x2="26" y2="91" stroke="#{c_neon}" stroke-width="1.3"/>
        <line x1="28" y1="11" x2="28" y2="89" stroke="#{c_dim}" stroke-width="0.7" opacity="0.6"/>

        <!-- Top Right Fold Corner -->
        <path d="M 62,8 L 62,24 L 78,24" fill="#16191f" stroke="#{c_neon}" stroke-width="1.6" stroke-linejoin="round"/>
        <line x1="62" y1="8" x2="78" y2="24" stroke="#{c_dim}" stroke-width="0.9"/>

        <!-- Bottom Label Banner Box -->
        <rect x="26" y="69" width="52" height="19" rx="1" fill="#16191f" stroke="#{c_neon}" stroke-width="2.4" opacity="0.35"/>
        <rect x="26" y="69" width="52" height="19" rx="1" fill="#16191f" stroke="#{c_neon}" stroke-width="1.5"/>
        <rect x="27.5" y="70.5" width="49" height="16" rx="0.5" fill="none" stroke="#{c_dim}" stroke-width="0.6" opacity="0.5"/>

        <!-- Text Label with Glow -->
        <text x="52" y="83" font-family="'DejaVu Sans', 'Liberation Sans', sans-serif" 
              font-size="10" font-weight="bold" fill="#{c_neon}" text-anchor="middle" letter-spacing="0.5"
              filter="drop-shadow(0px 0px 2px #{c_neon})">#{label_text}</text>

        <!-- Center Emblem -->
        <g filter="url(#neon-glow)" opacity="0.45">
          #{glyph_svg}
        </g>
        <g>
          #{glyph_svg}
        </g>
      </svg>
    SVG
  end

  # ----------------------------------------------------------------------------
  # 2. WIREFRAME FOLDER
  # ----------------------------------------------------------------------------
  def self.build_folder(c_neon, c_dim, glyph_svg)
    <<~SVG
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
        <defs>
          <filter id="folder-glow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="2.2" result="blur1"/>
            <feGaussianBlur stdDeviation="4.5" result="blur2"/>
            <feMerge>
              <feMergeNode in="blur2"/>
              <feMergeNode in="blur1"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>
        <path d="M 9,36 L 91,36 Q 93,36 92,39 L 88,81 Q 87,85 83,85 L 17,85 Q 13,85 12,81 L 8,39 Q 7,36 9,36 Z" 
              fill="none" stroke="#{c_neon}" stroke-width="4.5" opacity="0.3" filter="url(#folder-glow)"/>
        <path d="M 12,24 L 38,24 L 46,32 L 88,32 Q 91,32 91,35 L 91,80 Q 91,84 87,84 L 13,84 Q 9,84 9,80 L 9,28 Q 9,24 12,24 Z" 
              fill="#16191f" stroke="#{c_neon}" stroke-width="1.8" stroke-linejoin="round"/>
        <path d="M 12,24 L 38,24 L 46,32 L 88,32" fill="none" stroke="#{c_dim}" stroke-width="1.2"/>
        <path d="M 9,36 L 91,36 Q 93,36 92,39 L 88,81 Q 87,85 83,85 L 17,85 Q 13,85 12,81 L 8,39 Q 7,36 9,36 Z" 
              fill="#14171e" stroke="#{c_neon}" stroke-width="2.2" stroke-linejoin="round"/>
        <g filter="url(#folder-glow)" opacity="0.45">
          #{glyph_svg}
        </g>
        <g>
          #{glyph_svg}
        </g>
      </svg>
    SVG
  end

  # ----------------------------------------------------------------------------
  # 3. TRASH CAN
  # ----------------------------------------------------------------------------
  def self.build_trash(c_neon, c_dim, is_full = false)
    core = if is_full
      <<~FULL
        <circle cx="50" cy="54" r="14" fill="#{c_neon}" fill-opacity="0.2" stroke="#{c_neon}" stroke-width="1.8"/>
        <polygon points="50,44 60,60 40,60" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="50" y1="48" x2="50" y2="55" stroke="#{c_dim}" stroke-width="1.5" stroke-linecap="round"/>
        <circle cx="50" cy="58" r="1" fill="#{c_neon}"/>
      FULL
    else
      <<~EMPTY
        <g transform="translate(50, 54) scale(0.9)">
          <polygon points="0,-12 12,8 -12,8" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
          <line x1="0" y1="-6" x2="0" y2="2" stroke="#{c_dim}" stroke-width="1.5" stroke-linecap="round"/>
          <circle cx="0" cy="5" r="1" fill="#{c_neon}"/>
        </g>
      EMPTY
    end

    <<~SVG
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
        <defs>
          <filter id="trash-glow" x="-30%" y="-30%" width="160%" height="160%">
            <feGaussianBlur stdDeviation="2.2" result="blur1"/>
            <feGaussianBlur stdDeviation="4.5" result="blur2"/>
            <feMerge>
              <feMergeNode in="blur2"/>
              <feMergeNode in="blur1"/>
              <feMergeNode in="SourceGraphic"/>
            </feMerge>
          </filter>
        </defs>
        <path d="M 26,25 L 74,25 L 70,84 Q 69,88 64,88 L 36,88 Q 31,88 30,84 Z" 
              fill="none" stroke="#{c_neon}" stroke-width="4" opacity="0.3" filter="url(#trash-glow)"/>
        <rect x="38" y="12" width="24" height="6" rx="2" fill="#16191f" stroke="#{c_dim}" stroke-width="1.5"/>
        <rect x="22" y="18" width="56" height="7" rx="3" fill="#16191f" stroke="#{c_neon}" stroke-width="2"/>
        <line x1="26" y1="21.5" x2="74" y2="21.5" stroke="#{c_dim}" stroke-width="1"/>
        <path d="M 26,25 L 74,25 L 70,84 Q 69,88 64,88 L 36,88 Q 31,88 30,84 Z" 
              fill="#16191f" stroke="#{c_neon}" stroke-width="2.2" stroke-linejoin="round"/>
        <line x1="32" y1="28" x2="35" y2="82" stroke="#{c_dim}" stroke-width="1.2"/>
        <line x1="68" y1="28" x2="65" y2="82" stroke="#{c_dim}" stroke-width="1.2"/>
        <line x1="42" y1="32" x2="42" y2="76" stroke="#{c_dim}" stroke-width="1.2" stroke-dasharray="4,3"/>
        <line x1="58" y1="32" x2="58" y2="76" stroke="#{c_dim}" stroke-width="1.2" stroke-dasharray="4,3"/>
        #{core}
      </svg>
    SVG
  end

  # ----------------------------------------------------------------------------
  # 4. SYMBOLIC ICONS
  # ----------------------------------------------------------------------------
  def self.build_symbolic(c_neon, glyph_svg)
    <<~SVG
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" width="100%" height="100%">
        #{glyph_svg}
      </svg>
    SVG
  end

  # ============================================================================
  # EMBLEMS (MIMETYPES)
  # ============================================================================
  def self.glyph_gr(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="0,-21 21,-10 21,10 0,21 -21,10 -21,-10" fill="none" stroke="#{c_neon}" stroke-width="1.8" stroke-linejoin="round"/>
        <polygon points="0,-16 16,-8 16,8 0,16 -16,8 -16,-8" fill="none" stroke="#{c_dim}" stroke-width="0.8"/>
        <text x="0" y="6" font-family="'DejaVu Sans', sans-serif" font-weight="900" font-size="15" fill="#{c_neon}" text-anchor="middle" letter-spacing="1">GR</text>
      </g>
    GLYPH
  end

  def self.glyph_ruby(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42) scale(1.05)">
        <polygon points="-10,-15 10,-15 22,-3 0,18 -22,-3" fill="none" stroke="#{c_neon}" stroke-width="1.7" stroke-linejoin="round"/>
        <polygon points="-5,-15 5,-15 0,-7" fill="none" stroke="#{c_neon}" stroke-width="1.1"/>
        <line x1="-22" y1="-3" x2="22" y2="-3" stroke="#{c_neon}" stroke-width="1.5"/>
        <line x1="-22" y1="-3" x2="0" y2="18" stroke="#{c_neon}" stroke-width="1.4"/>
        <line x1="0" y1="-3" x2="0" y2="18" stroke="#{c_neon}" stroke-width="1.3"/>
        <line x1="22" y1="-3" x2="0" y2="18" stroke="#{c_neon}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_python(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42) scale(0.95)">
        <path d="M 0,-18 C -6.5,-18 -12,-14 -12,-8 L -12,-3.5 L 3.5,-3.5 L 3.5,0 L -11.5,0 C -16.5,0 -18,5 -18,9.5 L -13,9.5 C -13,4.5 -10.5,3.5 -5.5,3.5 L 3.5,3.5 C 9,3.5 12,0 12,-4 L 12,-8 C 12,-14 6.5,-18 0,-18 Z" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="-6" cy="-11" r="1.6" fill="#{c_neon}"/>
        <path d="M 0,18 C 6.5,18 12,14 12,8 L 12,3.5 L -3.5,3.5 L -3.5,0 L 11.5,0 C 16.5,0 18,-5 18,-9.5 L 13,-9.5 C 13,-4.5 10.5,-3.5 5.5,-3.5 L -3.5,-3.5 C -9,-3.5 -12,0 -12,4 L -12,8 C -12,14 -6.5,18 0,18 Z" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="6" cy="11" r="1.6" fill="#{c_neon}"/>
      </g>
    GLYPH
  end

  def self.glyph_json(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42) scale(0.95)">
        <path d="M -6,-18 Q -14,-18 -14,-11 L -14,-5 Q -14,-1 -18,0 Q -14,1 -14,5 L -14,11 Q -14,18 -6,18 L -6,14 Q -10,14 -10,10 L -10,4 Q -10,0 -15,0 Q -10,0 -10,-4 L -10,-10 Q -10,-14 -6,-14 Z" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <path d="M 6,-18 Q 14,-18 14,-11 L 14,-5 Q 14,-1 18,0 Q 14,1 14,5 L 14,11 Q 14,18 6,18 L 6,14 Q 10,14 10,10 L 10,4 Q 10,0 15,0 Q 10,0 10,-4 L 10,-10 Q 10,-14 6,-14 Z" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
      </g>
    GLYPH
  end

  def self.glyph_badge(c_neon, c_dim, text_str, font_sz = 16)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-20" y="-16" width="40" height="32" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <rect x="-17" y="-13" width="34" height="26" rx="1.5" fill="none" stroke="#{c_dim}" stroke-width="0.7"/>
        <text x="0" y="6" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="#{font_sz}" fill="#{c_neon}" text-anchor="middle">#{text_str}</text>
      </g>
    GLYPH
  end

  def self.glyph_hex(c_neon, c_dim, text_str, font_sz = 14)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="0,-19 18,-9.5 18,9.5 0,19 -18,9.5 -18,-9.5" fill="none" stroke="#{c_neon}" stroke-width="1.6" stroke-linejoin="round"/>
        <polygon points="0,-14 13,-7 13,7 0,14 -13,7 -13,-7" fill="none" stroke="#{c_dim}" stroke-width="0.8"/>
        <text x="0" y="5.5" font-family="'DejaVu Sans', sans-serif" font-weight="900" font-size="#{font_sz}" fill="#{c_neon}" text-anchor="middle">#{text_str}</text>
      </g>
    GLYPH
  end

  def self.glyph_doc(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-17" y="-15" width="34" height="28" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <rect x="-14" y="-12" width="28" height="22" rx="1" fill="none" stroke="#{c_dim}" stroke-width="0.7"/>
        <text x="0" y="6.5" font-family="'DejaVu Serif', Georgia, serif" font-weight="bold" font-size="17" fill="#{c_neon}" text-anchor="middle">W</text>
      </g>
    GLYPH
  end

  def self.glyph_xls(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-17" y="-15" width="34" height="28" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <line x1="-17" y1="-5" x2="17" y2="-5" stroke="#{c_neon}" stroke-width="1.2"/>
        <line x1="-17" y1="5" x2="17" y2="5" stroke="#{c_dim}" stroke-width="1"/>
        <line x1="-6" y1="-15" x2="-6" y2="13" stroke="#{c_neon}" stroke-width="1.2"/>
        <line x1="5" y1="-15" x2="5" y2="13" stroke="#{c_dim}" stroke-width="1"/>
      </g>
    GLYPH
  end

  def self.glyph_ppt(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-18" y="-14" width="36" height="24" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <line x1="-7" y1="13" x2="7" y2="13" stroke="#{c_neon}" stroke-width="1.6" stroke-linecap="round"/>
        <line x1="0" y1="10" x2="0" y2="13" stroke="#{c_dim}" stroke-width="1.4"/>
        <circle cx="0" cy="-2" r="7.5" fill="none" stroke="#{c_dim}" stroke-width="1.2"/>
        <path d="M 0,-2 L 0,-9.5 A 7.5,7.5 0 0 1 6.5,2 Z" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_epub(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <path d="M 0,-12 Q -9,-14 -18,-11 L -18,11 Q -9,8 0,10 Q 9,8 18,11 L 18,-11 Q 9,-14 0,-12 Z" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="0" y1="-12" x2="0" y2="10" stroke="#{c_dim}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_3d(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="0,-18 16,-9 16,9 0,18 -16,9 -16,-9" fill="none" stroke="#{c_neon}" stroke-width="1.6" stroke-linejoin="round"/>
        <line x1="0" y1="-18" x2="0" y2="0" stroke="#{c_dim}" stroke-width="1.2"/>
        <line x1="0" y1="0" x2="16" y2="9" stroke="#{c_dim}" stroke-width="1.2"/>
        <line x1="0" y1="0" x2="-16" y2="9" stroke="#{c_dim}" stroke-width="1.2"/>
      </g>
    GLYPH
  end

  def self.glyph_font(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <text x="-4" y="6" font-family="'DejaVu Serif', Georgia, serif" font-weight="bold" font-size="21" fill="#{c_neon}" text-anchor="middle">A</text>
        <text x="8" y="7" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="14" fill="#{c_dim}" text-anchor="middle">a</text>
      </g>
    GLYPH
  end

  def self.glyph_ipynb(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <ellipse cx="0" cy="0" rx="16" ry="8" fill="none" stroke="#{c_neon}" stroke-width="1.5" transform="rotate(-25)"/>
        <ellipse cx="0" cy="0" rx="16" ry="8" fill="none" stroke="#{c_dim}" stroke-width="1.2" transform="rotate(35)"/>
        <circle cx="0" cy="0" r="4" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
      </g>
    GLYPH
  end

  def self.glyph_service(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <circle cx="0" cy="0" r="14" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="-16" y1="0" x2="16" y2="0" stroke="#{c_neon}" stroke-width="1.8" stroke-linecap="round"/>
        <line x1="0" y1="-16" x2="0" y2="16" stroke="#{c_neon}" stroke-width="1.8" stroke-linecap="round"/>
        <polygon points="2,-8 -3,0 1,0 -2,8 4,-1 0,-1" fill="#{c_neon}" stroke="#{c_dim}" stroke-width="0.8"/>
      </g>
    GLYPH
  end

  def self.glyph_pcap(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <path d="M -16,12 C -12,2 -4,-10 12,-14 C 8,-2 10,6 16,12 C 4,12 -6,8 -16,12 Z" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="2" fill="#{c_neon}"/>
        <line x1="-12" y1="8" x2="12" y2="8" stroke="#{c_dim}" stroke-width="1"/>
      </g>
    GLYPH
  end

  def self.glyph_ino(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <ellipse cx="-8" cy="0" rx="9" ry="8" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <ellipse cx="8" cy="0" rx="9" ry="8" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <text x="-8" y="3.5" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="11" fill="#{c_neon}" text-anchor="middle">-</text>
        <text x="8" y="4.5" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="11" fill="#{c_neon}" text-anchor="middle">+</text>
      </g>
    GLYPH
  end

  def self.glyph_k8s(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="0,-16 14,-7 14,7 0,16 -14,7 -14,-7" fill="none" stroke="#{c_neon}" stroke-width="1.6" stroke-linejoin="round"/>
        <circle cx="0" cy="0" r="5" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_game(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-18" y="-12" width="36" height="24" rx="6" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="-10" y1="-4" x2="-10" y2="4" stroke="#{c_neon}" stroke-width="1.6" stroke-linecap="round"/>
        <line x1="-14" y1="0" x2="-6" y2="0" stroke="#{c_neon}" stroke-width="1.6" stroke-linecap="round"/>
        <circle cx="10" cy="-3" r="2" fill="#{c_neon}"/>
        <circle cx="7" cy="2" r="2" fill="#{c_dim}"/>
        <circle cx="13" cy="2" r="2" fill="#{c_dim}"/>
      </g>
    GLYPH
  end

  def self.glyph_sub(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-18" y="-13" width="36" height="26" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <text x="0" y="6" font-family="'DejaVu Sans', sans-serif" font-weight="900" font-size="14" fill="#{c_neon}" text-anchor="middle">CC</text>
      </g>
    GLYPH
  end

  def self.glyph_sql(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <ellipse cx="0" cy="-10" rx="16" ry="5" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <path d="M -16,-10 L -16,0 A 16,5 0 0 0 16,0 L 16,-10" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <path d="M -16,0 L -16,10 A 16,5 0 0 0 16,10 L 16,0" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
      </g>
    GLYPH
  end

  def self.glyph_docker(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42) scale(0.95)">
        <rect x="-14" y="-12" width="6" height="5" fill="none" stroke="#{c_neon}" stroke-width="1.2"/>
        <rect x="-6" y="-12" width="6" height="5" fill="none" stroke="#{c_neon}" stroke-width="1.2"/>
        <rect x="2" y="-12" width="6" height="5" fill="none" stroke="#{c_neon}" stroke-width="1.2"/>
        <rect x="-6" y="-18" width="6" height="5" fill="none" stroke="#{c_neon}" stroke-width="1.2"/>
        <rect x="2" y="-18" width="6" height="5" fill="none" stroke="#{c_neon}" stroke-width="1.2"/>
        <rect x="10" y="-12" width="6" height="5" fill="none" stroke="#{c_neon}" stroke-width="1.2"/>
        <path d="M -18,-5 L 18,-5 C 20,-5 22,-2 22,2 C 22,10 14,14 0,14 C -12,14 -18,8 -18,2 Z" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="16" cy="0" r="1" fill="#{c_neon}"/>
      </g>
    GLYPH
  end

  def self.glyph_lua(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <circle cx="-2" cy="2" r="13" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="11" cy="-11" r="4.5" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_rust(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <circle cx="0" cy="0" r="15" fill="none" stroke="#{c_neon}" stroke-width="1.7"/>
        <circle cx="0" cy="0" r="11" fill="none" stroke="#{c_dim}" stroke-width="1" stroke-dasharray="3,2"/>
        <text x="0" y="6.5" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="17" fill="#{c_neon}" text-anchor="middle">R</text>
      </g>
    GLYPH
  end

  def self.glyph_java(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42) scale(1.05)">
        <path d="M -9,2 L 7,2 L 5,14 Q 4,17 0,17 Q -4,17 -5,14 Z" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <path d="M 7,4 C 11,4 11,11 7,11" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <path d="M -3,-9 Q 0,-5 -3,-1" fill="none" stroke="#{c_neon}" stroke-width="1.4" stroke-linecap="round"/>
        <path d="M 3,-9 Q 6,-5 3,-1" fill="none" stroke="#{c_dim}" stroke-width="1.4" stroke-linecap="round"/>
      </g>
    GLYPH
  end

  def self.glyph_swift(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42) scale(0.95)">
        <path d="M -16,14 C -16,6 -6,-6 14,-14 C 6,-6 4,6 10,14 C 2,6 -4,8 -6,14 C -8,10 -12,12 -16,14 Z" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
      </g>
    GLYPH
  end

  def self.glyph_dart(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="-14,-14 6,-14 16,-4 6,14 -14,14 -4,0" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
      </g>
    GLYPH
  end

  def self.glyph_vue(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="-18,-14 18,-14 0,16" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <polygon points="-11,-14 11,-14 0,4" fill="none" stroke="#{c_dim}" stroke-width="1.2"/>
      </g>
    GLYPH
  end

  def self.glyph_svelte(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <path d="M 6,-14 C 12,-14 14,-9 14,-4 C 14,4 4,6 4,11 C 4,14 7,15 11,15 C 15,15 17,12 17,12 L 15,17 C 15,17 12,19 7,19 C 1,19 -1,14 -1,9 C -1,1 9,-1 9,-6 C 9,-9 7,-10 4,-10 C 1,-10 -2,-7 -2,-7 L -4,-12 C -4,-12 0,-14 6,-14 Z" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
      </g>
    GLYPH
  end

  def self.glyph_sol(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="0,-18 13,-2 0,6 -13,-2" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <polygon points="0,9 13,3 0,19 -13,3" fill="none" stroke="#{c_dim}" stroke-width="1.5"/>
      </g>
    GLYPH
  end

  def self.glyph_exe(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="0,-18 17,-9 17,9 0,18 -17,9 -17,-9" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <text x="0" y="5.5" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="14" fill="#{c_neon}" text-anchor="middle">EXE</text>
      </g>
    GLYPH
  end

  def self.glyph_desktop(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-18" y="-14" width="36" height="25" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <polygon points="0,-9 5,2 0,0 -5,2" fill="none" stroke="#{c_dim}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_key(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <circle cx="-6" cy="0" r="9" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="3" y1="0" x2="18" y2="0" stroke="#{c_neon}" stroke-width="1.8"/>
        <line x1="12" y1="0" x2="12" y2="6" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="16" y1="0" x2="16" y2="4" stroke="#{c_dim}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_pkg(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="0,-18 16,-9 16,9 0,18 -16,9 -16,-9" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="0" y1="-18" x2="0" y2="18" stroke="#{c_dim}" stroke-width="1.2"/>
        <line x1="0" y1="0" x2="16" y2="-9" stroke="#{c_dim}" stroke-width="1.2"/>
        <line x1="0" y1="0" x2="-16" y2="-9" stroke="#{c_dim}" stroke-width="1.2"/>
      </g>
    GLYPH
  end

  def self.glyph_iso(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <circle cx="0" cy="0" r="16" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="0" cy="0" r="5" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
        <circle cx="0" cy="0" r="2" fill="#{c_neon}"/>
      </g>
    GLYPH
  end

  def self.glyph_make(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <circle cx="0" cy="0" r="13" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="-16" y1="0" x2="16" y2="0" stroke="#{c_neon}" stroke-width="2" stroke-linecap="round"/>
        <line x1="0" y1="-16" x2="0" y2="16" stroke="#{c_neon}" stroke-width="2" stroke-linecap="round"/>
      </g>
    GLYPH
  end

  def self.glyph_git(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <circle cx="-6" cy="-8" r="3.5" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <circle cx="-6" cy="8" r="3.5" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <circle cx="8" cy="0" r="3.5" fill="none" stroke="#{c_dim}" stroke-width="1.5"/>
        <line x1="-6" y1="-4.5" x2="-6" y2="4.5" stroke="#{c_neon}" stroke-width="1.6"/>
        <path d="M -6,8 Q 0,8 8,0" fill="none" stroke="#{c_dim}" stroke-width="1.6"/>
      </g>
    GLYPH
  end

  def self.glyph_lock(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-14" y="-3" width="28" height="20" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <path d="M -8,-3 L -8,-10 C -8,-15 8,-15 8,-10 L 8,-3" fill="none" stroke="#{c_dim}" stroke-width="1.6"/>
        <circle cx="0" cy="6" r="2.5" fill="#{c_neon}"/>
      </g>
    GLYPH
  end

  def self.glyph_sh(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-19" y="-15" width="38" height="30" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <text x="0" y="7" font-family="monospace, monospace" font-weight="bold" font-size="20" fill="#{c_neon}" text-anchor="middle">&gt;_</text>
      </g>
    GLYPH
  end

  def self.glyph_html(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="-15,-17 15,-17 11,15 0,19 -11,15" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <text x="0" y="7" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="17" fill="#{c_neon}" text-anchor="middle">5</text>
      </g>
    GLYPH
  end

  def self.glyph_css(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <polygon points="-15,-17 15,-17 11,15 0,19 -11,15" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <text x="0" y="8" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="20" fill="#{c_neon}" text-anchor="middle">#</text>
      </g>
    GLYPH
  end

  def self.glyph_php(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <ellipse cx="0" cy="0" rx="19" ry="13" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <text x="0" y="5.5" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="14" fill="#{c_neon}" text-anchor="middle">php</text>
      </g>
    GLYPH
  end

  def self.glyph_md(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-19" y="-14" width="38" height="28" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <text x="0" y="6.5" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="17" fill="#{c_neon}" text-anchor="middle">MD</text>
      </g>
    GLYPH
  end

  def self.glyph_pdf(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-19" y="-14" width="38" height="28" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <text x="0" y="5.5" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="15" fill="#{c_neon}" text-anchor="middle">PDF</text>
      </g>
    GLYPH
  end

  def self.glyph_zip(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-17" y="-15" width="34" height="30" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="0" y1="-15" x2="0" y2="3" stroke="#{c_dim}" stroke-width="1.4" stroke-dasharray="3,2"/>
        <rect x="-4" y="3" width="8" height="6" rx="1.5" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_txt(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <line x1="-15" y1="-11" x2="15" y2="-11" stroke="#{c_neon}" stroke-width="1.6" stroke-linecap="round"/>
        <line x1="-15" y1="-3" x2="15" y2="-3" stroke="#{c_dim}" stroke-width="1.4" stroke-linecap="round"/>
        <line x1="-15" y1="5" x2="15" y2="5" stroke="#{c_neon}" stroke-width="1.6" stroke-linecap="round"/>
      </g>
    GLYPH
  end

  def self.glyph_dll(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <circle cx="0" cy="0" r="15" fill="none" stroke="#{c_neon}" stroke-width="1.7"/>
        <text x="0" y="5.5" font-family="'DejaVu Sans', sans-serif" font-weight="bold" font-size="12" fill="#{c_neon}" text-anchor="middle">DLL</text>
      </g>
    GLYPH
  end

  def self.glyph_vector(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <path d="M -14,14 L -4,-12 L 14,-14 L 12,4 Z" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="-14" cy="14" r="2" fill="#{c_neon}"/>
        <circle cx="-4" cy="-12" r="2" fill="#{c_neon}"/>
        <circle cx="14" cy="-14" r="2" fill="#{c_neon}"/>
        <circle cx="12" cy="4" r="2" fill="#{c_neon}"/>
      </g>
    GLYPH
  end

  def self.glyph_image(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-18" y="-14" width="36" height="28" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="-8" cy="-5" r="3" fill="none" stroke="#{c_dim}" stroke-width="1.2"/>
        <polygon points="-14,10 -4,-2 4,6 8,2 14,10" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.glyph_audio(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <line x1="-16" y1="-3" x2="-16" y2="3" stroke="#{c_dim}" stroke-width="1.8" stroke-linecap="round"/>
        <line x1="-10" y1="-8" x2="-10" y2="8" stroke="#{c_neon}" stroke-width="1.8" stroke-linecap="round"/>
        <line x1="-4" y1="-14" x2="-4" y2="14" stroke="#{c_dim}" stroke-width="1.8" stroke-linecap="round"/>
        <line x1="2" y1="-18" x2="2" y2="18" stroke="#{c_neon}" stroke-width="2" stroke-linecap="round"/>
        <line x1="8" y1="-11" x2="8" y2="11" stroke="#{c_dim}" stroke-width="1.8" stroke-linecap="round"/>
        <line x1="14" y1="-4" x2="14" y2="4" stroke="#{c_neon}" stroke-width="1.8" stroke-linecap="round"/>
      </g>
    GLYPH
  end

  def self.glyph_video(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-18" y="-14" width="36" height="28" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <polygon points="-5,-8 8,0 -5,8" fill="none" stroke="#{c_neon}" stroke-width="1.6" stroke-linejoin="round"/>
      </g>
    GLYPH
  end

  def self.glyph_config(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <line x1="-16" y1="-8" x2="16" y2="-8" stroke="#{c_dim}" stroke-width="1.4" stroke-linecap="round"/>
        <circle cx="-5" cy="-8" r="3.5" fill="#16191f" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="-16" y1="0" x2="16" y2="0" stroke="#{c_dim}" stroke-width="1.4" stroke-linecap="round"/>
        <circle cx="6" cy="0" r="3.5" fill="#16191f" stroke="#{c_neon}" stroke-width="1.6"/>
        <line x1="-16" y1="8" x2="16" y2="8" stroke="#{c_dim}" stroke-width="1.4" stroke-linecap="round"/>
        <circle cx="-8" cy="8" r="3.5" fill="#16191f" stroke="#{c_neon}" stroke-width="1.6"/>
      </g>
    GLYPH
  end

  def self.glyph_xml(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-19" y="-15" width="38" height="30" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <text x="0" y="6" font-family="'DejaVu Sans', monospace" font-weight="bold" font-size="14" fill="#{c_neon}" text-anchor="middle">XML</text>
      </g>
    GLYPH
  end

  def self.glyph_code(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(52, 42)">
        <rect x="-19" y="-16" width="38" height="32" rx="3" fill="none" stroke="#{c_neon}" stroke-width="1.5"/>
        <text x="0" y="7" font-family="'DejaVu Sans', monospace" font-weight="900" font-size="18" fill="#{c_neon}" text-anchor="middle">&lt;/&gt;</text>
      </g>
    GLYPH
  end

  # ============================================================================
  # EMBLEMS (PLACES FOLDERS)
  # ============================================================================
  def self.folder_glyph_home(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <polygon points="0,-16 18,0 12,0 12,12 -12,12 -12,0 -18,0" fill="none" stroke="#{c_neon}" stroke-width="1.8" stroke-linejoin="round"/>
        <rect x="-4" y="0" width="8" height="12" fill="none" stroke="#{c_dim}" stroke-width="1.2"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_dragon(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <polygon points="0,-14 14,-7 14,7 0,14 -14,7 -14,-7" fill="none" stroke="#{c_neon}" stroke-width="1.8"/>
        <circle cx="0" cy="0" r="4" fill="none" stroke="#{c_dim}" stroke-width="1.4"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_python(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.7)">
        <path d="M 0,-14 C -5,-14 -9,-11 -9,-6 L -9,-3 L 3,-3 L 3,0 L -9,0 C -13,0 -14,4 -14,8 L -10,8 C -10,4 -8,3 -4,3 L 3,3 C 7,3 9,0 9,-3 L 9,-6 C 9,-11 5,-14 0,-14 Z" fill="none" stroke="#{c_neon}" stroke-width="2"/>
        <path d="M 0,14 C 5,14 9,11 9,6 L 9,3 L -3,3 L -3,0 L 9,0 C 13,0 14,-4 14,-8 L 10,-8 C 10,-4 8,-3 4,-3 L -3,-3 C -7,-3 -9,0 -9,3 L -9,6 C -9,11 -5,14 0,14 Z" fill="none" stroke="#{c_neon}" stroke-width="2"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_downloads(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <polygon points="-4,-12 4,-12 4,-2 10,-2 0,9 -10,-2 -4,-2" fill="none" stroke="#{c_neon}" stroke-width="1.8" stroke-linejoin="round"/>
        <line x1="-12" y1="12" x2="12" y2="12" stroke="#{c_dim}" stroke-width="1.8" stroke-linecap="round"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_documents(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <rect x="-10" y="-12" width="20" height="24" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.8"/>
        <line x1="-6" y1="-6" x2="6" y2="-6" stroke="#{c_dim}" stroke-width="1.4" stroke-linecap="round"/>
        <line x1="-6" y1="0" x2="6" y2="0" stroke="#{c_neon}" stroke-width="1.4" stroke-linecap="round"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_desktop(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <rect x="-14" y="-10" width="28" height="18" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.8"/>
        <line x1="-5" y1="12" x2="5" y2="12" stroke="#{c_dim}" stroke-width="1.8" stroke-linecap="round"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_music(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <path d="M -6,-10 L 8,-13 L 8,4 A 4,3.5 0 1 1 4,0.5 L 4,-8 L -6,-5.5 L -6,7 A 4,3.5 0 1 1 -10,3.5 L -10,-9 Q -10,-10 -6,-10 Z" fill="none" stroke="#{c_neon}" stroke-width="1.8"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_pictures(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <rect x="-14" y="-10" width="28" height="20" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.8"/>
        <circle cx="-6" cy="-4" r="2.5" fill="none" stroke="#{c_dim}" stroke-width="1.4"/>
        <polygon points="-11,7 -4,-2 2,4 6,0 11,6 11,7" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_videos(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <rect x="-14" y="-10" width="28" height="20" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.8"/>
        <polygon points="-3,-5 6,0 -3,5" fill="none" stroke="#{c_neon}" stroke-width="1.8"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_templates(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <rect x="-12" y="-12" width="24" height="24" rx="2" fill="none" stroke="#{c_neon}" stroke-width="1.6" stroke-dasharray="4,2"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_public(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <circle cx="0" cy="0" r="12" fill="none" stroke="#{c_neon}" stroke-width="1.8"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_code(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <polygon points="-11,0 -5,-7 -3,-5 -7,0 -3,5 -5,7" fill="#{c_neon}"/>
        <polygon points="11,0 5,-7 3,-5 7,0 3,5 5,7" fill="#{c_neon}"/>
      </g>
    GLYPH
  end

  def self.folder_glyph_git(c_neon, c_dim)
    <<~GLYPH
      <g transform="translate(50, 60) scale(0.95)">
        <circle cx="-6" cy="-7" r="3" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="-6" cy="7" r="3" fill="none" stroke="#{c_neon}" stroke-width="1.6"/>
        <circle cx="7" cy="0" r="3" fill="none" stroke="#{c_dim}" stroke-width="1.6"/>
        <line x1="-6" y1="-4" x2="-6" y2="4" stroke="#{c_neon}" stroke-width="1.6"/>
        <path d="M -6,7 Q 0,7 7,0" fill="none" stroke="#{c_dim}" stroke-width="1.6"/>
      </g>
    GLYPH
  end

  # ============================================================================
  # SYMBOLIC GLYPHS (16x16)
  # ============================================================================
  def self.sym_home(c_neon)
    <<~SVG
      <path d="M 8,1.5 L 14,7 L 12,7 L 12,14.5 L 4,14.5 L 4,7 L 2,7 Z" fill="none" stroke="#{c_neon}" stroke-width="1.4" stroke-linejoin="round"/>
      <rect x="6.5" y="9" width="3" height="5.5" fill="#{c_neon}"/>
    SVG
  end

  def self.sym_folder(c_neon)
    <<~SVG
      <path d="M 1.5,3 L 6,3 L 7.5,5 L 14.5,5 L 14.5,13.5 L 1.5,13.5 Z" fill="none" stroke="#{c_neon}" stroke-width="1.4" stroke-linejoin="round"/>
    SVG
  end

  def self.sym_desktop(c_neon)
    <<~SVG
      <rect x="1.5" y="2.5" width="13" height="9" rx="1" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      <line x1="5" y1="13.5" x2="11" y2="13.5" stroke="#{c_neon}" stroke-width="1.4" stroke-linecap="round"/>
      <line x1="8" y1="11.5" x2="8" y2="13.5" stroke="#{c_neon}" stroke-width="1.4"/>
    SVG
  end

  def self.sym_downloads(c_neon)
    <<~SVG
      <polygon points="5,2 11,2 11,7 14,7 8,13 2,7 5,7" fill="none" stroke="#{c_neon}" stroke-width="1.3" stroke-linejoin="round"/>
      <line x1="2" y1="14.5" x2="14" y2="14.5" stroke="#{c_neon}" stroke-width="1.4" stroke-linecap="round"/>
    SVG
  end

  def self.sym_documents(c_neon)
    <<~SVG
      <path d="M 3,1.5 L 10,1.5 L 13,4.5 L 13,14.5 L 3,14.5 Z" fill="none" stroke="#{c_neon}" stroke-width="1.4" stroke-linejoin="round"/>
      <line x1="5.5" y1="7" x2="10.5" y2="7" stroke="#{c_neon}" stroke-width="1.2" stroke-linecap="round"/>
    SVG
  end

  def self.sym_music(c_neon)
    <<~SVG
      <path d="M 4,2 L 12,1 L 12,11 A 2.5,2.5 0 1 1 9.5,8.5 L 9.5,4 L 4,5 L 4,12 A 2.5,2.5 0 1 1 1.5,9.5 L 1.5,2 Z" fill="#{c_neon}"/>
    SVG
  end

  def self.sym_pictures(c_neon)
    <<~SVG
      <rect x="1.5" y="2.5" width="13" height="11" rx="1.5" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      <circle cx="5" cy="5.5" r="1.5" fill="#{c_neon}"/>
      <polygon points="3,12 7,7 10,10 12,8 13,9.5 13,12" fill="#{c_neon}"/>
    SVG
  end

  def self.sym_videos(c_neon)
    <<~SVG
      <rect x="1.5" y="2.5" width="13" height="11" rx="1.5" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      <polygon points="6,5 11,8 6,11" fill="#{c_neon}"/>
    SVG
  end

  def self.sym_trash(c_neon)
    <<~SVG
      <rect x="2" y="3" width="12" height="2" rx="1" fill="#{c_neon}"/>
      <path d="M 3.5,5 L 12.5,5 L 11.5,14.5 L 4.5,14.5 Z" fill="none" stroke="#{c_neon}" stroke-width="1.4" stroke-linejoin="round"/>
    SVG
  end

  def self.sym_disk(c_neon)
    <<~SVG
      <rect x="1.5" y="4" width="13" height="8" rx="1.5" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      <circle cx="4" cy="8" r="1" fill="#{c_neon}"/>
    SVG
  end

  def self.sym_network(c_neon)
    <<~SVG
      <circle cx="8" cy="4" r="2.5" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      <circle cx="3" cy="12" r="2" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      <circle cx="13" cy="12" r="2" fill="none" stroke="#{c_neon}" stroke-width="1.4"/>
      <line x1="8" y1="6.5" x2="8" y2="9.5" stroke="#{c_neon}" stroke-width="1.2"/>
    SVG
  end
end

# Find all base Flat-Remix mimetypes
REMIX_MIMES = Dir.glob(["/usr/share/icons/Flat-Remix-Red-Dark/mimetypes/scalable/*.svg", 
                        "/usr/share/icons/Flat-Remix-Red-Dark/scalable/mimetypes/*.svg",
                        "/usr/share/icons/Flat-Remix-Blue-Dark/mimetypes/scalable/*.svg",
                        "/usr/share/icons/Flat-Remix-Blue-Dark/scalable/mimetypes/*.svg"]).map { |f| File.basename(f, ".svg") }.uniq

puts "=" * 78
puts "🐉 COMPILANDO SUITE DE ICONOS UNIVERSAL MASTER OMNIVERSE COMPLETA"
puts "Total de tipos MIME base a sobreescribir: #{REMIX_MIMES.size}"
puts "=" * 78


threads = COLORS.map do |key, c|
  Thread.new do
  theme_name = "Kali-Dragon-Icons-#{c[:name]}"
  variant_icons_dir = File.join(VARIANTS_DIR, key, "desktop", "icons", theme_name)
  user_icons_dir = File.expand_path("~/.local/share/icons/#{theme_name}")

  [variant_icons_dir, user_icons_dir].each do |dest_root|
    places_dir    = File.join(dest_root, "scalable", "places")
    devices_dir   = File.join(dest_root, "scalable", "devices")
    apps_dir      = File.join(dest_root, "scalable", "apps")
    actions_dir   = File.join(dest_root, "scalable", "actions")
    mimes_dir     = File.join(dest_root, "scalable", "mimetypes")
    status_dir    = File.join(dest_root, "scalable", "status")
    sym_dir       = File.join(dest_root, "symbolic", "places")
    sym_act_dir   = File.join(dest_root, "symbolic", "actions")
    sym_dev_dir   = File.join(dest_root, "symbolic", "devices")
    sym_stat_dir  = File.join(dest_root, "symbolic", "status")

    [places_dir, devices_dir, apps_dir, actions_dir, mimes_dir, status_dir, sym_dir, sym_act_dir, sym_dev_dir, sym_stat_dir].each { |d| FileUtils.mkdir_p(d) }

    # index.theme
    File.write(File.join(dest_root, "index.theme"), <<~INI)
      [Icon Theme]
      Name=#{theme_name}
      Comment=Kali Dragon Cyberpunk Neon Wireframe Icon Suite (#{c[:name]} Edition)
      Inherits=#{c[:inherit]},Flat-Remix-Blue-Dark,Papirus-Dark,Adwaita,hicolor
      Directories=scalable/places,scalable/devices,scalable/apps,scalable/actions,scalable/mimetypes,scalable/status,symbolic/places,symbolic/actions,symbolic/devices,symbolic/status

      [scalable/places]
      Size=64
      Context=Places
      Type=Scalable
      MinSize=16
      MaxSize=512

      [scalable/devices]
      Size=64
      Context=Devices
      Type=Scalable
      MinSize=16
      MaxSize=512

      [scalable/apps]
      Size=64
      Context=Applications
      Type=Scalable
      MinSize=16
      MaxSize=512

      [scalable/actions]
      Size=64
      Context=Actions
      Type=Scalable
      MinSize=16
      MaxSize=512

      [scalable/mimetypes]
      Size=64
      Context=MimeTypes
      Type=Scalable
      MinSize=16
      MaxSize=512

      [scalable/status]
      Size=64
      Context=Status
      Type=Scalable
      MinSize=16
      MaxSize=512

      [symbolic/places]
      Size=16
      Context=Places
      Type=Scalable
      MinSize=16
      MaxSize=512

      [symbolic/actions]
      Size=16
      Context=Actions
      Type=Scalable
      MinSize=16
      MaxSize=512

      [symbolic/devices]
      Size=16
      Context=Devices
      Type=Scalable
      MinSize=16
      MaxSize=512

      [symbolic/status]
      Size=16
      Context=Status
      Type=Scalable
      MinSize=16
      MaxSize=512
    INI

    # 1. FOLDERS & PLACES
    f_generic = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_dragon(c[:neon], c[:dim]))
    f_home    = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_home(c[:neon], c[:dim]))
    f_desk    = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_desktop(c[:neon], c[:dim]))
    f_down    = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_downloads(c[:neon], c[:dim]))
    f_docs    = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_documents(c[:neon], c[:dim]))
    f_music   = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_music(c[:neon], c[:dim]))
    f_pics    = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_pictures(c[:neon], c[:dim]))
    f_vids    = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_videos(c[:neon], c[:dim]))
    f_temp    = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_templates(c[:neon], c[:dim]))
    f_pub     = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_public(c[:neon], c[:dim]))
    f_dev     = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_code(c[:neon], c[:dim]))
    f_git     = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_git(c[:neon], c[:dim]))
    f_pyenv   = GeminiWireframeFactory.build_folder(c[:neon], c[:dim], GeminiWireframeFactory.folder_glyph_python(c[:neon], c[:dim]))

    %w[folder folder-open inode-directory gtk-directory gnome-folder folder-saved-search folder-recent document-open-recent].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_generic) }
    %w[user-home folder-home gnome-home gnome-fs-home folder-personal go-home user-bookmarks folder-me user-me].each do |n|
      File.write(File.join(places_dir, "#{n}.svg"), f_home)
      File.write(File.join(actions_dir, "#{n}.svg"), f_home)
    end
    %w[user-desktop folder-desktop desktop cs-desktop gnome-fs-desktop].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_desk) }
    %w[folder-download folder-downloads folder_download].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_down) }
    %w[folder-documents folder-document folder-text].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_docs) }
    %w[folder-music folder-sound library-music].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_music) }
    %w[folder-pictures folder-images user-pictures user-images user-image folder-camera].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_pics) }
    %w[folder-videos folder-video].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_vids) }
    %w[folder-templates folder-template].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_temp) }
    %w[folder-publicshare folder-public user-share].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_pub) }
    %w[folder-development folder-development-git folder-projects folder-project folder-code folder-script].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_dev) }
    %w[folder-git folder-github].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_git) }
    %w[folder-python folder-venv folder-virtualenv folder-environment].each { |n| File.write(File.join(places_dir, "#{n}.svg"), f_pyenv) }

    # 2. STANDALONE TRASH CAN
    trash_empty = GeminiWireframeFactory.build_trash(c[:neon], c[:dim], false)
    trash_full  = GeminiWireframeFactory.build_trash(c[:neon], c[:dim], true)

    [places_dir, status_dir].each do |t_dir|
      File.write(File.join(t_dir, "user-trash.svg"), trash_empty)
      File.write(File.join(t_dir, "user-trash-full.svg"), trash_full)
      File.write(File.join(t_dir, "trashcan_empty.svg"), trash_empty)
      File.write(File.join(t_dir, "trashcan_full.svg"), trash_full)
      File.write(File.join(t_dir, "emptytrash.svg"), trash_empty)
      File.write(File.join(t_dir, "trash.svg"), trash_empty)
      File.write(File.join(t_dir, "xfce-trash_empty.svg"), trash_empty)
      File.write(File.join(t_dir, "xfce-trash_full.svg"), trash_full)
      File.write(File.join(t_dir, "xfce4-trash-plugin.svg"), trash_empty)
    end

    # 3. SYMBOLIC ICONS
    s_home    = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_home(c[:neon]))
    s_folder  = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_folder(c[:neon]))
    s_desk    = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_desktop(c[:neon]))
    s_down    = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_downloads(c[:neon]))
    s_docs    = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_documents(c[:neon]))
    s_music   = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_music(c[:neon]))
    s_pics    = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_pictures(c[:neon]))
    s_vids    = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_videos(c[:neon]))
    s_trash   = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_trash(c[:neon]))
    s_disk    = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_disk(c[:neon]))
    s_net     = GeminiWireframeFactory.build_symbolic(c[:neon], GeminiWireframeFactory.sym_network(c[:neon]))

    [sym_dir, places_dir, sym_act_dir, actions_dir].each do |dest|
      File.write(File.join(dest, "user-home-symbolic.svg"), s_home)
      File.write(File.join(dest, "folder-home-symbolic.svg"), s_home)
      File.write(File.join(dest, "folder-personal-symbolic.svg"), s_home)
      File.write(File.join(dest, "go-home-symbolic.svg"), s_home)
      File.write(File.join(dest, "user-bookmarks-symbolic.svg"), s_home)
      File.write(File.join(dest, "folder-symbolic.svg"), s_folder)
      File.write(File.join(dest, "user-desktop-symbolic.svg"), s_desk)
      File.write(File.join(dest, "folder-desktop-symbolic.svg"), s_desk)
      File.write(File.join(dest, "folder-download-symbolic.svg"), s_down)
      File.write(File.join(dest, "folder-downloads-symbolic.svg"), s_down)
      File.write(File.join(dest, "folder-documents-symbolic.svg"), s_docs)
      File.write(File.join(dest, "folder-music-symbolic.svg"), s_music)
      File.write(File.join(dest, "folder-pictures-symbolic.svg"), s_pics)
      File.write(File.join(dest, "folder-videos-symbolic.svg"), s_vids)
      File.write(File.join(dest, "user-trash-symbolic.svg"), s_trash)
      File.write(File.join(dest, "user-trash-full-symbolic.svg"), s_trash)
    end

    [sym_dev_dir, devices_dir].each do |dest|
      File.write(File.join(dest, "drive-harddisk-symbolic.svg"), s_disk)
      File.write(File.join(dest, "drive-harddisk.svg"), s_disk)
      File.write(File.join(dest, "drive-removable-media-symbolic.svg"), s_disk)
      File.write(File.join(dest, "drive-removable-media.svg"), s_disk)
      File.write(File.join(dest, "media-flash.svg"), s_disk)
      File.write(File.join(dest, "computer-symbolic.svg"), s_desk)
      File.write(File.join(dest, "computer.svg"), s_desk)
      File.write(File.join(dest, "network-workgroup.svg"), s_net)
      File.write(File.join(dest, "network-server-symbolic.svg"), s_net)
      File.write(File.join(dest, "network-server.svg"), s_net)
    end

    # 4. INSTANTIATE MASTER GLYPH MAP
    doc_map = {
      # Custom GR Family
      "gr"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "gr", GeminiWireframeFactory.glyph_gr(c[:neon], c[:dim])),
      "gry"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "gry", GeminiWireframeFactory.glyph_gr(c[:neon], c[:dim])),

      # Ruby Family
      "ruby"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ruby", GeminiWireframeFactory.glyph_ruby(c[:neon], c[:dim])),
      "erb"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "erb", GeminiWireframeFactory.glyph_ruby(c[:neon], c[:dim])),
      "rake"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "rake", GeminiWireframeFactory.glyph_ruby(c[:neon], c[:dim])),

      # Python Family
      "python"    => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "py", GeminiWireframeFactory.glyph_python(c[:neon], c[:dim])),
      "pyw"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "pyw", GeminiWireframeFactory.glyph_python(c[:neon], c[:dim])),
      "pyx"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "pyx", GeminiWireframeFactory.glyph_python(c[:neon], c[:dim])),
      "pyi"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "pyi", GeminiWireframeFactory.glyph_python(c[:neon], c[:dim])),

      # C & C++ Family
      "c"         => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "c", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "C", 16)),
      "h"         => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "h", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "H", 16)),
      "cpp"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "cpp", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "C++", 13.5)),
      "hpp"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "hpp", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "H++", 13)),

      # C# & .NET Family
      "cs"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "cs", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "C#", 14)),
      "vb"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "vb", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "VB", 14)),
      "fs"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "fs", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "F#", 14)),

      # JavaScript & TypeScript Family
      "js"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "js", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "JS", 19)),
      "jsx"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "jsx", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "JSX", 15)),
      "ts"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ts", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "TS", 19)),
      "tsx"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "tsx", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "TSX", 15)),

      # CSS Family
      "css"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "css", GeminiWireframeFactory.glyph_css(c[:neon], c[:dim])),
      "scss"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "scss", GeminiWireframeFactory.glyph_css(c[:neon], c[:dim])),
      "sass"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "sass", GeminiWireframeFactory.glyph_css(c[:neon], c[:dim])),
      "less"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "less", GeminiWireframeFactory.glyph_css(c[:neon], c[:dim])),
      "styl"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "styl", GeminiWireframeFactory.glyph_css(c[:neon], c[:dim])),

      # Systemd Services Family
      "service"   => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "service", GeminiWireframeFactory.glyph_service(c[:neon], c[:dim])),
      "timer"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "timer", GeminiWireframeFactory.glyph_service(c[:neon], c[:dim])),
      "socket"    => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "socket", GeminiWireframeFactory.glyph_service(c[:neon], c[:dim])),
      "target"    => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "target", GeminiWireframeFactory.glyph_service(c[:neon], c[:dim])),
      "mount"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "mount", GeminiWireframeFactory.glyph_service(c[:neon], c[:dim])),
      "swap"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "swap", GeminiWireframeFactory.glyph_service(c[:neon], c[:dim])),

      # Game Dev Family
      "gd"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "gd", GeminiWireframeFactory.glyph_game(c[:neon], c[:dim])),
      "tscn"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "tscn", GeminiWireframeFactory.glyph_game(c[:neon], c[:dim])),
      "tres"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "tres", GeminiWireframeFactory.glyph_game(c[:neon], c[:dim])),
      "godot"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "godot", GeminiWireframeFactory.glyph_game(c[:neon], c[:dim])),
      "unity"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "unity", GeminiWireframeFactory.glyph_game(c[:neon], c[:dim])),

      # Database Family
      "sql"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "sql", GeminiWireframeFactory.glyph_sql(c[:neon], c[:dim])),
      "sqlite"    => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "sqlite", GeminiWireframeFactory.glyph_sql(c[:neon], c[:dim])),
      "db"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "db", GeminiWireframeFactory.glyph_sql(c[:neon], c[:dim])),

      # DevOps & Infrastructure Family
      "docker"    => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "docker", GeminiWireframeFactory.glyph_docker(c[:neon], c[:dim])),
      "k8s"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "k8s", GeminiWireframeFactory.glyph_k8s(c[:neon], c[:dim])),
      "tf"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "tf", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "TF", 16)),
      "make"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "make", GeminiWireframeFactory.glyph_make(c[:neon], c[:dim])),
      "cmake"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "cmake", GeminiWireframeFactory.glyph_make(c[:neon], c[:dim])),
      "ci"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ci", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "CI", 16)),

      # Git Family
      "git"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "git", GeminiWireframeFactory.glyph_git(c[:neon], c[:dim])),
      "diff"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "diff", GeminiWireframeFactory.glyph_git(c[:neon], c[:dim])),

      # Cybersecurity & Forensics Family
      "pcap"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "pcap", GeminiWireframeFactory.glyph_pcap(c[:neon], c[:dim])),
      "key"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "key", GeminiWireframeFactory.glyph_key(c[:neon], c[:dim])),
      "cert"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "cert", GeminiWireframeFactory.glyph_key(c[:neon], c[:dim])),
      "kdbx"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "kdbx", GeminiWireframeFactory.glyph_key(c[:neon], c[:dim])),
      "yara"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "yar", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "YAR", 15)),
      "vpn"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "vpn", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "VPN", 15)),

      # Hardware & Microcontrollers Family
      "ino"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ino", GeminiWireframeFactory.glyph_ino(c[:neon], c[:dim])),
      "hex"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "hex", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "HEX", 13)),
      "vhd"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "vhd", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "VHD", 14)),
      "v"         => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "v", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "V", 16)),

      # Office Family
      "doc"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "doc", GeminiWireframeFactory.glyph_doc(c[:neon], c[:dim])),
      "odt"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "odt", GeminiWireframeFactory.glyph_doc(c[:neon], c[:dim])),
      "rtf"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "rtf", GeminiWireframeFactory.glyph_doc(c[:neon], c[:dim])),
      "pages"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "pages", GeminiWireframeFactory.glyph_doc(c[:neon], c[:dim])),

      # Spreadsheets Family
      "xls"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "xls", GeminiWireframeFactory.glyph_xls(c[:neon], c[:dim])),
      "ods"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ods", GeminiWireframeFactory.glyph_xls(c[:neon], c[:dim])),
      "csv"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "csv", GeminiWireframeFactory.glyph_xls(c[:neon], c[:dim])),
      "tsv"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "tsv", GeminiWireframeFactory.glyph_xls(c[:neon], c[:dim])),

      # Presentations Family
      "ppt"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ppt", GeminiWireframeFactory.glyph_ppt(c[:neon], c[:dim])),
      "odp"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "odp", GeminiWireframeFactory.glyph_ppt(c[:neon], c[:dim])),
      "keynote"   => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "key", GeminiWireframeFactory.glyph_ppt(c[:neon], c[:dim])),

      # Ebooks & Comics Family
      "epub"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "epub", GeminiWireframeFactory.glyph_epub(c[:neon], c[:dim])),
      "mobi"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "mobi", GeminiWireframeFactory.glyph_epub(c[:neon], c[:dim])),
      "djvu"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "djvu", GeminiWireframeFactory.glyph_epub(c[:neon], c[:dim])),
      "cbr"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "cbr", GeminiWireframeFactory.glyph_epub(c[:neon], c[:dim])),
      "cbz"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "cbz", GeminiWireframeFactory.glyph_epub(c[:neon], c[:dim])),

      # 3D & CAD Family
      "3d"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "3d", GeminiWireframeFactory.glyph_3d(c[:neon], c[:dim])),
      "3ds"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "3ds", GeminiWireframeFactory.glyph_3d(c[:neon], c[:dim])),
      "blend"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "blend", GeminiWireframeFactory.glyph_3d(c[:neon], c[:dim])),
      "obj"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "obj", GeminiWireframeFactory.glyph_3d(c[:neon], c[:dim])),
      "stl"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "stl", GeminiWireframeFactory.glyph_3d(c[:neon], c[:dim])),
      "gltf"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "gltf", GeminiWireframeFactory.glyph_3d(c[:neon], c[:dim])),
      "dxf"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "dxf", GeminiWireframeFactory.glyph_3d(c[:neon], c[:dim])),
      "step"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "step", GeminiWireframeFactory.glyph_3d(c[:neon], c[:dim])),

      # Shell & Terminal Family
      "sh"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "sh", GeminiWireframeFactory.glyph_sh(c[:neon], c[:dim])),
      "bash"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "bash", GeminiWireframeFactory.glyph_sh(c[:neon], c[:dim])),
      "zsh"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "zsh", GeminiWireframeFactory.glyph_sh(c[:neon], c[:dim])),
      "ps1"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ps1", GeminiWireframeFactory.glyph_sh(c[:neon], c[:dim])),
      "bat"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "bat", GeminiWireframeFactory.glyph_sh(c[:neon], c[:dim])),

      # Subtitles Family
      "sub"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "sub", GeminiWireframeFactory.glyph_sub(c[:neon], c[:dim])),
      "srt"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "srt", GeminiWireframeFactory.glyph_sub(c[:neon], c[:dim])),
      "vtt"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "vtt", GeminiWireframeFactory.glyph_sub(c[:neon], c[:dim])),
      "ass"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ass", GeminiWireframeFactory.glyph_sub(c[:neon], c[:dim])),

      # Executables, Packages & AppImages
      "exe"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "exe", GeminiWireframeFactory.glyph_exe(c[:neon], c[:dim])),
      "appimage"  => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "app", GeminiWireframeFactory.glyph_pkg(c[:neon], c[:dim])),
      "pkg"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "pkg", GeminiWireframeFactory.glyph_pkg(c[:neon], c[:dim])),
      "iso"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "iso", GeminiWireframeFactory.glyph_iso(c[:neon], c[:dim])),
      "desktop"   => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "desktop", GeminiWireframeFactory.glyph_desktop(c[:neon], c[:dim])),
      "dll"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "dll", GeminiWireframeFactory.glyph_dll(c[:neon], c[:dim])),

      # Other Standalone Languages & Formats
      "java"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "java", GeminiWireframeFactory.glyph_java(c[:neon], c[:dim])),
      "swift"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "swift", GeminiWireframeFactory.glyph_swift(c[:neon], c[:dim])),
      "kt"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "kt", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "KT", 14)),
      "dart"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "dart", GeminiWireframeFactory.glyph_dart(c[:neon], c[:dim])),
      "rust"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "rust", GeminiWireframeFactory.glyph_rust(c[:neon], c[:dim])),
      "go"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "go", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "GO", 16)),
      "lua"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "lua", GeminiWireframeFactory.glyph_lua(c[:neon], c[:dim])),
      "php"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "php", GeminiWireframeFactory.glyph_php(c[:neon], c[:dim])),
      "html"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "html", GeminiWireframeFactory.glyph_html(c[:neon], c[:dim])),
      "vue"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "vue", GeminiWireframeFactory.glyph_vue(c[:neon], c[:dim])),
      "svelte"    => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "svelte", GeminiWireframeFactory.glyph_svelte(c[:neon], c[:dim])),
      "astro"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "astro", GeminiWireframeFactory.glyph_svelte(c[:neon], c[:dim])),
      "zig"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "zig", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "ZIG", 13)),
      "sol"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "sol", GeminiWireframeFactory.glyph_sol(c[:neon], c[:dim])),
      "mat"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "mat", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "MAT", 15)),
      "json"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "json", GeminiWireframeFactory.glyph_json(c[:neon], c[:dim])),
      "yaml"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "yaml", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "YML", 15)),
      "xml"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "xml", GeminiWireframeFactory.glyph_xml(c[:neon], c[:dim])),
      "md"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "md", GeminiWireframeFactory.glyph_md(c[:neon], c[:dim])),
      "pdf"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "pdf", GeminiWireframeFactory.glyph_pdf(c[:neon], c[:dim])),
      "zip"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "zip", GeminiWireframeFactory.glyph_zip(c[:neon], c[:dim])),
      "txt"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "txt", GeminiWireframeFactory.glyph_txt(c[:neon], c[:dim])),
      "font"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "font", GeminiWireframeFactory.glyph_font(c[:neon], c[:dim])),
      "ipynb"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ipynb", GeminiWireframeFactory.glyph_ipynb(c[:neon], c[:dim])),
      "lock"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "lock", GeminiWireframeFactory.glyph_lock(c[:neon], c[:dim])),
      "svg"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "svg", GeminiWireframeFactory.glyph_vector(c[:neon], c[:dim])),
      "img"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "img", GeminiWireframeFactory.glyph_image(c[:neon], c[:dim])),
      "audio"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "audio", GeminiWireframeFactory.glyph_audio(c[:neon], c[:dim])),
      "video"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "video", GeminiWireframeFactory.glyph_video(c[:neon], c[:dim])),
      "cfg"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "cfg", GeminiWireframeFactory.glyph_config(c[:neon], c[:dim])),
      "pl"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "pl", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "PL", 16)),
      "hs"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "hs", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "HS", 14)),
      "scala"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "scala", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "SC", 16)),
      "clj"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "clj", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "CLJ", 14)),
      "ex"        => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "ex", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "EX", 16)),
      "erl"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "erl", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "ERL", 14)),
      "r"         => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "r", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "R", 17)),
      "julia"     => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "julia", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "JL", 16)),
      "nim"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "nim", GeminiWireframeFactory.glyph_hex(c[:neon], c[:dim], "NIM", 13)),
      "asm"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "asm", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "ASM", 14)),
      "tex"       => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "tex", GeminiWireframeFactory.glyph_badge(c[:neon], c[:dim], "TEX", 14)),
      "code"      => GeminiWireframeFactory.build_doc(c[:neon], c[:dim], "code", GeminiWireframeFactory.glyph_code(c[:neon], c[:dim]))
    }

    # Classifier
    classify = ->(m) do
      ml = m.downcase
      if ml.include?("ruby") || ml.include?("gem")
        doc_map["ruby"]
      elsif ml.include?("rake")
        doc_map["rake"]
      elsif ml.include?("erb")
        doc_map["erb"]
      elsif ml.include?("pyw")
        doc_map["pyw"]
      elsif ml.include?("pyx")
        doc_map["pyx"]
      elsif ml.include?("pyi")
        doc_map["pyi"]
      elsif ml.include?("python") || ml.include?("pyc") || ml.include?("pyo")
        doc_map["python"]
      elsif ml.include?("tsx")
        doc_map["tsx"]
      elsif ml.include?("typescript") || ml.include?("linguist") || ml.include?("text-ts")
        doc_map["ts"]
      elsif ml.include?("jsx")
        doc_map["jsx"]
      elsif ml.include?("javascript") || ml.include?("text-js") || ml.include?("application-js") || ml.include?("node")
        doc_map["js"]
      elsif ml.include?("json")
        doc_map["json"]
      elsif ml.include?("yaml") || ml.include?("yml")
        doc_map["yaml"]
      elsif ml.include?("hpp") || ml.include?("c++hdr") || ml.include?("c++-header")
        doc_map["hpp"]
      elsif ml.include?("c++") || ml.include?("cpp") || ml.include?("cxx")
        doc_map["cpp"]
      elsif ml.include?("chdr") || ml.include?("c-header")
        doc_map["h"]
      elsif %w[text-x-c text-x-csrc text-c application-x-c c].include?(ml)
        doc_map["c"]
      elsif ml.include?("csharp") || ml.include?("cs-source") || ml.include?("c#")
        doc_map["cs"]
      elsif ml.include?("scss")
        doc_map["scss"]
      elsif ml.include?("sass")
        doc_map["sass"]
      elsif ml.include?("less")
        doc_map["less"]
      elsif ml.include?("styl")
        doc_map["styl"]
      elsif ml.include?("css")
        doc_map["css"]
      elsif ml.include?("powershell") || ml.include?("ps1")
        doc_map["ps1"]
      elsif ml.include?("batch") || ml.include?("bat") || ml.include?("cmd")
        doc_map["bat"]
      elsif ml.include?("timer")
        doc_map["timer"]
      elsif ml.include?("socket")
        doc_map["socket"]
      elsif ml.include?("target")
        doc_map["target"]
      elsif ml.include?("mount")
        doc_map["mount"]
      elsif ml.include?("swap")
        doc_map["swap"]
      elsif ml.include?("systemd") || ml.include?("service")
        doc_map["service"]
      elsif ml.include?("tscn") || ml.include?("escn")
        doc_map["tscn"]
      elsif ml.include?("tres")
        doc_map["tres"]
      elsif ml.include?("godot")
        doc_map["godot"]
      elsif ml.include?("unity") || ml.include?("prefab")
        doc_map["unity"]
      elsif ml.include?("gdscript") || ml.include?("game")
        doc_map["gd"]
      elsif ml.include?("sqlite")
        doc_map["sqlite"]
      elsif ml.include?("sql") || ml.include?("database")
        doc_map["sql"]
      elsif ml.include?("tsv") || ml.include?("tab-separated")
        doc_map["tsv"]
      elsif ml.include?("csv")
        doc_map["csv"]
      elsif ml.include?("ods") || ml.include?("calc")
        doc_map["ods"]
      elsif ml.include?("excel") || ml.include?("spreadsheet") || ml.include?("sheet")
        doc_map["xls"]
      elsif ml.include?("odt") || ml.include?("abiword")
        doc_map["odt"]
      elsif ml.include?("rtf")
        doc_map["rtf"]
      elsif ml.include?("pages")
        doc_map["pages"]
      elsif ml.include?("word") || ml.include?("msword") || ml.include?("opendocument.text") || ml.include?("document")
        doc_map["doc"]
      elsif ml.include?("odp") || ml.include?("impress")
        doc_map["odp"]
      elsif ml.include?("keynote")
        doc_map["keynote"]
      elsif ml.include?("powerpoint") || ml.include?("presentation")
        doc_map["ppt"]
      elsif ml.include?("comicbook-rar") || ml.include?("cbr")
        doc_map["cbr"]
      elsif ml.include?("comicbook") || ml.include?("cbz")
        doc_map["cbz"]
      elsif ml.include?("mobi") || ml.include?("azw")
        doc_map["mobi"]
      elsif ml.include?("djvu")
        doc_map["djvu"]
      elsif ml.include?("epub") || ml.include?("ebook")
        doc_map["epub"]
      elsif ml.include?("blend")
        doc_map["blend"]
      elsif ml.include?("3ds")
        doc_map["3ds"]
      elsif ml.include?("obj")
        doc_map["obj"]
      elsif ml.include?("stl")
        doc_map["stl"]
      elsif ml.include?("gltf") || ml.include?("glb")
        doc_map["gltf"]
      elsif ml.include?("dxf")
        doc_map["dxf"]
      elsif ml.include?("step") || ml.include?("stp")
        doc_map["step"]
      elsif ml.include?("3d") || ml.include?("model-") || ml.include?("cad")
        doc_map["3d"]
      elsif ml.include?("bash")
        doc_map["bash"]
      elsif ml.include?("zsh")
        doc_map["zsh"]
      elsif ml.include?("shell")
        doc_map["sh"]
      elsif ml.include?("srt") || ml.include?("subrip")
        doc_map["srt"]
      elsif ml.include?("vtt")
        doc_map["vtt"]
      elsif ml.include?("ssa") || ml.include?("ass")
        doc_map["ass"]
      elsif ml.include?("subtitle") || ml.include?("subviewer")
        doc_map["sub"]
      elsif ml.include?("pcap") || ml.include?("tcpdump") || ml.include?("wireshark")
        doc_map["pcap"]
      elsif ml.include?("arduino") || ml.include?("ino")
        doc_map["ino"]
      elsif ml.include?("k8s") || ml.include?("kubernetes") || ml.include?("helm")
        doc_map["k8s"]
      elsif ml.include?("tf") || ml.include?("terraform") || ml.include?("hcl")
        doc_map["tf"]
      elsif ml.include?("cmake")
        doc_map["cmake"]
      elsif ml.include?("makefile")
        doc_map["make"]
      elsif ml.include?("ci") || ml.include?("jenkins") || ml.include?("gitlab")
        doc_map["ci"]
      elsif ml.include?("patch") || ml.include?("diff")
        doc_map["diff"]
      elsif ml.include?("git")
        doc_map["git"]
      elsif ml.include?("cert") || ml.include?("crt") || ml.include?("pem") || ml.include?("x509")
        doc_map["cert"]
      elsif ml.include?("kdbx") || ml.include?("keepass")
        doc_map["kdbx"]
      elsif ml.include?("key") || ml.include?("gpg") || ml.include?("pkcs")
        doc_map["key"]
      elsif ml.include?("yara")
        doc_map["yara"]
      elsif ml.include?("vpn") || ml.include?("ovpn")
        doc_map["vpn"]
      elsif ml.include?("vhdl")
        doc_map["vhd"]
      elsif ml.include?("verilog")
        doc_map["v"]
      elsif ml.include?("hex") || ml.include?("elf")
        doc_map["hex"]
      elsif ml.include?("appimage")
        doc_map["appimage"]
      elsif ml.include?("java") || ml.include?("jar") || ml.include?("class")
        doc_map["java"]
      elsif ml.include?("swift")
        doc_map["swift"]
      elsif ml.include?("kotlin")
        doc_map["kt"]
      elsif ml.include?("dart")
        doc_map["dart"]
      elsif ml.include?("rust")
        doc_map["rust"]
      elsif ml.include?("golang") || ml.include?("go")
        doc_map["go"]
      elsif ml.include?("lua")
        doc_map["lua"]
      elsif ml.include?("php")
        doc_map["php"]
      elsif ml.include?("html") || ml.include?("xhtml")
        doc_map["html"]
      elsif ml.include?("vue")
        doc_map["vue"]
      elsif ml.include?("astro")
        doc_map["astro"]
      elsif ml.include?("svelte")
        doc_map["svelte"]
      elsif ml.include?("zig")
        doc_map["zig"]
      elsif ml.include?("solidity")
        doc_map["sol"]
      elsif ml.include?("matlab") || ml.include?("octave") || ml.include?("hdf")
        doc_map["mat"]
      elsif ml.include?("pdf")
        doc_map["pdf"]
      elsif ml.include?("zip") || ml.include?("tar") || ml.include?("archive") || ml.include?("7z") || ml.include?("rar") || ml.include?("gzip") || ml.include?("bzip") || ml.include?("xz")
        doc_map["zip"]
      elsif ml.include?("font") || ml.include?("ttf") || ml.include?("otf") || ml.include?("woff")
        doc_map["font"]
      elsif ml.include?("ipynb") || ml.include?("jupyter")
        doc_map["ipynb"]
      elsif ml.include?("ms-dos") || ml.include?("msdos") || ml.include?("wine") || ml.include?("exe")
        doc_map["exe"]
      elsif ml.include?("sharedlib") || ml.include?("dll") || ml.include?("so")
        doc_map["dll"]
      elsif ml.include?("deb") || ml.include?("rpm") || ml.include?("apk") || ml.include?("package")
        doc_map["pkg"]
      elsif ml.include?("cd-image") || ml.include?("iso") || ml.include?("diskimage")
        doc_map["iso"]
      elsif ml.include?("lock")
        doc_map["lock"]
      elsif ml.include?("svg") || ml.include?("illustrator") || ml.include?("vector")
        doc_map["svg"]
      elsif ml.include?("image") || ml.include?("png") || ml.include?("jpeg") || ml.include?("jpg") || ml.include?("webp") || ml.include?("gif") || ml.include?("bmp") || ml.include?("ico") || ml.include?("psd") || ml.include?("xcf")
        doc_map["img"]
      elsif ml.include?("audio") || ml.include?("mp3") || ml.include?("wav") || ml.include?("flac") || ml.include?("ogg") || ml.include?("midi")
        doc_map["audio"]
      elsif ml.include?("video") || ml.include?("mp4") || ml.include?("mkv") || ml.include?("avi") || ml.include?("webm")
        doc_map["video"]
      elsif ml.include?("config") || ml.include?("ini") || ml.include?("conf") || ml.include?("env") || ml.include?("toml")
        doc_map["cfg"]
      elsif ml.include?("xml") || ml.include?("plist")
        doc_map["xml"]
      elsif ml.include?("md") || ml.include?("markdown")
        doc_map["md"]
      elsif ml.include?("plain") || ml.include?("text-x-generic") || ml.include?("readme") || ml.include?("log")
        doc_map["txt"]
      else
        doc_map["code"]
      end
    end

    # Write all mapped Flat-Remix mimetypes
    REMIX_MIMES.each do |mime_name|
      doc_svg = classify.call(mime_name)
      File.write(File.join(mimes_dir, "#{mime_name}.svg"), doc_svg)
    end

    # Explicit Overrides for ZERO Fallback
    extra_explicit = [
      # GR Family
      [doc_map["gr"],        %w[text-x-gr application-x-gr application-gr text-gr gr]],
      [doc_map["gry"],       %w[text-x-gry gry]],

      # Ruby Family
      [doc_map["ruby"],      %w[text-x-ruby application-x-ruby text-ruby application-ruby application-x-ruby-gem application-x-gem text-x-gemfile text-x-ruby-source ruby gemfile]],
      [doc_map["erb"],       %w[text-x-erb text-x-ruby-erb application-x-erb text-html-ruby erb rhtml]],
      [doc_map["rake"],      %w[text-x-rake text-x-rakefile rakefile rake]],

      # Python Family
      [doc_map["python"],    %w[text-x-python text-x-python3 application-x-python application-x-python3 text-python text-python3 gnome-mime-text-x-python application-x-python-bytecode python python3 x-python text-x-python-source py]],
      [doc_map["pyw"],       %w[text-x-python-gui pyw]],
      [doc_map["pyx"],       %w[text-x-cython pyx pxd]],
      [doc_map["pyi"],       %w[text-x-python-stub pyi]],

      # C & C++ Family
      [doc_map["c"],         %w[text-x-c text-x-csrc text-c application-x-c c]],
      [doc_map["h"],         %w[text-x-chdr text-x-c-header h]],
      [doc_map["cpp"],       %w[text-x-c++ text-x-c++src text-c++ application-x-c++ text-x-cpp text-x-c++-source cpp cc cxx]],
      [doc_map["hpp"],       %w[text-x-c++hdr text-x-c++-header hpp hh hxx inl tpp]],

      # C# & .NET Family
      [doc_map["cs"],        %w[text-x-csharp application-x-csharp text-csharp csharp cs]],
      [doc_map["vb"],        %w[text-x-vb text-x-vbs application-x-vb vb vbs]],
      [doc_map["fs"],        %w[text-x-fsharp fs fsx]],

      # JavaScript & TypeScript Family
      [doc_map["js"],        %w[application-javascript text-javascript application-x-javascript text-x-javascript text-js text-x-js application-x-js js mjs cjs]],
      [doc_map["jsx"],       %w[text-x-jsx text-jsx application-x-jsx application-jsx jsx]],
      [doc_map["ts"],        %w[text-vnd.trolltech.linguist application-typescript text-typescript application-x-typescript text-x-typescript text-ts text-x-ts ts mts cts]],
      [doc_map["tsx"],       %w[application-x-tiled-tsx text-x-tsx text-tsx application-x-tsx application-tsx tsx]],

      # CSS Family
      [doc_map["css"],       %w[text-css text-x-css css]],
      [doc_map["scss"],      %w[text-x-scss scss]],
      [doc_map["sass"],      %w[text-x-sass sass]],
      [doc_map["less"],      %w[text-x-less less]],
      [doc_map["styl"],      %w[text-x-stylus styl]],

      # Systemd Services Family
      [doc_map["service"],   %w[text-x-systemd-service text-x-systemd-unit application-x-systemd-unit systemd service]],
      [doc_map["timer"],     %w[text-x-systemd-timer timer]],
      [doc_map["socket"],    %w[text-x-systemd-socket socket]],
      [doc_map["target"],    %w[text-x-systemd-target target]],
      [doc_map["mount"],     %w[text-x-systemd-mount mount automount]],
      [doc_map["swap"],      %w[text-x-systemd-swap swap]],

      # Game Dev Family
      [doc_map["gd"],        %w[text-x-gdscript gd]],
      [doc_map["tscn"],      %w[application-x-godot-scene text-x-godot-scene tscn escn]],
      [doc_map["tres"],      %w[text-x-godot-resource tres]],
      [doc_map["godot"],     %w[application-x-godot-project godot]],
      [doc_map["unity"],     %w[text-x-unity unity prefab asset]],

      # Database Family
      [doc_map["sql"],       %w[application-x-sql text-x-sql application-sql text-sql psql mysql sql]],
      [doc_map["sqlite"],    %w[application-x-sqlite3 application-vnd.sqlite3 sqlite sqlite3 s3db]],
      [doc_map["db"],        %w[application-x-database db]],

      # DevOps & Infrastructure Family
      [doc_map["docker"],    %w[text-x-dockerfile application-x-docker-compose text-dockerfile dockerfile docker containerfile]],
      [doc_map["k8s"],       %w[text-x-kubernetes application-x-kubernetes k8s]],
      [doc_map["tf"],        %w[text-x-terraform text-terraform tf tfvars hcl]],
      [doc_map["make"],      %w[text-x-makefile makefile make]],
      [doc_map["cmake"],     %w[text-x-cmake text-x-cmakeinfo cmake]],
      [doc_map["ci"],        %w[text-x-ci jenkinsfile]],

      # Git Family
      [doc_map["git"],       %w[text-x-git text-x-git-config git]],
      [doc_map["diff"],      %w[text-x-patch diff patch]],

      # Cybersecurity Family
      [doc_map["pcap"],      %w[application-vnd.tcpdump.pcap application-x-pcap org.wireshark.Wireshark-mimetype pcap cap pcapng]],
      [doc_map["key"],       %w[application-x-key application-x-pem-key application-pgp-keys application-pkix-cert application-x-pkcs12 gpg key]],
      [doc_map["cert"],      %w[application-x-x509-ca-cert application-x-certificate cert crt pem]],
      [doc_map["kdbx"],      %w[application-x-keepass application-x-kdbx kdbx kdb]],
      [doc_map["yara"],      %w[application-x-yara text-x-yara yara yar]],
      [doc_map["vpn"],       %w[application-x-openvpn-profile vpn ovpn]],

      # Hardware Family
      [doc_map["ino"],       %w[text-x-arduino text-arduino ino]],
      [doc_map["hex"],       %w[application-x-hex hex bin elf rom]],
      [doc_map["vhd"],       %w[text-x-vhdl text-vhdl vhd vhdl]],
      [doc_map["v"],         %w[text-x-verilog text-verilog v sv]],

      # Office Family
      [doc_map["doc"],       %w[application-msword application-vnd.openxmlformats-officedocument.wordprocessingml.document x-office-document doc docx]],
      [doc_map["odt"],       %w[application-vnd.oasis.opendocument.text odt]],
      [doc_map["rtf"],       %w[application-rtf text-rtf application-x-rtf rtf]],
      [doc_map["pages"],     %w[application-vnd.apple.pages pages]],

      # Spreadsheets Family
      [doc_map["xls"],       %w[application-vnd.ms-excel application-vnd.openxmlformats-officedocument.spreadsheetml.sheet x-office-spreadsheet xls xlsx]],
      [doc_map["ods"],       %w[application-vnd.oasis.opendocument.spreadsheet ods]],
      [doc_map["csv"],       %w[text-csv application-csv csv]],
      [doc_map["tsv"],       %w[text-tab-separated-values text-tsv application-tsv tsv]],

      # Presentations Family
      [doc_map["ppt"],       %w[application-vnd.ms-powerpoint application-vnd.openxmlformats-officedocument.presentationml.presentation x-office-presentation ppt pptx]],
      [doc_map["odp"],       %w[application-vnd.oasis.opendocument.presentation odp]],
      [doc_map["keynote"],   %w[application-vnd.apple.keynote key keynote]],

      # Ebooks & Comics Family
      [doc_map["epub"],      %w[application-epub+zip epub]],
      [doc_map["mobi"],      %w[application-x-mobipocket-ebook mobi azw azw3]],
      [doc_map["djvu"],      %w[image-vnd.djvu djvu]],
      [doc_map["cbr"],       %w[application-vnd.comicbook-rar application-x-cbr application-x-comicbook-rar cbr]],
      [doc_map["cbz"],       %w[application-vnd.comicbook+zip application-x-cbz application-x-comicbook-zip cbz]],

      # 3D & CAD Family
      [doc_map["3ds"],       %w[application-x-nintendo-3ds-rom image-x-3ds model-3ds 3ds]],
      [doc_map["blend"],     %w[application-x-blender blend]],
      [doc_map["obj"],       %w[model-obj obj]],
      [doc_map["stl"],       %w[model-stl stl]],
      [doc_map["gltf"],      %w[model-gltf+json model-gltf-binary gltf glb]],
      [doc_map["dxf"],       %w[image-vnd.dxf dxf]],
      [doc_map["step"],      %w[model-step step stp]],

      # Shell Family
      [doc_map["sh"],        %w[application-x-shellscript text-x-script text-x-sh sh]],
      [doc_map["bash"],      %w[text-x-bash bash]],
      [doc_map["zsh"],       %w[text-x-zsh zsh]],
      [doc_map["ps1"],       %w[text-x-powershell application-x-powershell ps1 powershell]],
      [doc_map["bat"],       %w[text-x-batch application-x-msdos-batch bat cmd]],

      # Subtitles Family
      [doc_map["srt"],       %w[application-x-subrip srt]],
      [doc_map["vtt"],       %w[text-vtt vtt]],
      [doc_map["ass"],       %w[text-x-ssa ass]],
      [doc_map["sub"],       %w[text-x-subviewer sub]],

      # Executables, Packages & Launchers
      [doc_map["appimage"],  %w[application-vnd.appimage application-x-appimage appimage]],
      [doc_map["exe"],       %w[application-x-ms-dos-executable application-x-msdos-program application-x-wine-extension-exe application-x-exe exe]],
      [doc_map["desktop"],   %w[application-x-desktop application-x-template-desktop application-desktop desktop]],

      # Languages & Scientific
      [doc_map["swift"],     %w[text-x-swift text-swift swift]],
      [doc_map["vue"],       %w[text-x-vue text-vue vue]],
      [doc_map["svelte"],    %w[text-x-svelte text-svelte svelte]],
      [doc_map["astro"],     %w[text-x-astro astro]],
      [doc_map["zig"],       %w[text-x-zig zig]],
      [doc_map["sol"],       %w[text-x-solidity text-solidity sol]],
      [doc_map["r"],         %w[text-x-r text-r r]],
      [doc_map["mat"],       %w[text-x-matlab text-matlab application-x-hdf application-x-hdf5 h5 hdf5 mat m]]
    ]

    extra_explicit.each do |svg_content, names|
      names.each do |n|
        File.write(File.join(mimes_dir, "#{n}.svg"), svg_content)
        File.write(File.join(apps_dir, "#{n}.svg"), svg_content) if %w[exe desktop wine application-default-icon system-run].include?(n)
        File.write(File.join(devices_dir, "#{n}.svg"), svg_content) if %w[media-optical drive-optical application-vnd.efi.iso].include?(n)
      end
    end
  end
  puts "✔ Tema compendiado con éxito: #{theme_name}"
  end
end
threads.each(&:join)

puts "\nActualizando caché de GTK para la sesión activa..."
system("gtk-update-icon-cache -f -q ~/.local/share/icons/Kali-Dragon-Icons-Red 2>/dev/null || true")

puts "\n ¡15 EDICIONES UNIVERSALES MASTER OMNIVERSE RECOMPILADAS CON ÉXITO!"
