import { spawnSync } from 'node:child_process'
import fs from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const manimDir = path.join(root, 'docs', 'manim')
const args = process.argv.slice(2)

if (args.length !== 6 || args[0] !== '--file' || args[2] !== '--scene' || args[4] !== '--output') {
  console.error('Usage: pnpm docs:manim -- --file <scene.py> --scene <SceneName> --output <image.png>')
  process.exit(1)
}

const source = path.resolve(root, args[1])
const scene = args[3]
const output = path.resolve(manimDir, args[5])
const manim = path.join(root, '.manim-venv', 'bin', 'manim')

if (!fs.existsSync(source)) {
  console.error('Manim source not found: ' + source)
  process.exit(1)
}
if (!fs.existsSync(manim)) {
  console.error('Manim not found at ' + manim)
  console.error('Create it with: uv venv .manim-venv && uv pip install --python .manim-venv/bin/python manim')
  process.exit(1)
}

const mediaDir = fs.mkdtempSync(path.join(root, '.manim-media-'))
const result = spawnSync(
  manim,
  ['render', '-s', '--media_dir', mediaDir, '-r', '2400,1350', '-q', 'm', source, scene],
  { cwd: root, stdio: 'inherit' },
)

if (result.status !== 0) {
  fs.rmSync(mediaDir, { recursive: true, force: true })
  process.exit(result.status ?? 1)
}

const sceneDir = path.join(mediaDir, 'images', path.basename(source, '.py'))
const rendered = fs.readdirSync(sceneDir).find(
  (file) => file.startsWith(scene + '_ManimCE_v') && file.endsWith('.png'),
)
if (!rendered) {
  console.error('No rendered PNG found in ' + sceneDir)
  fs.rmSync(mediaDir, { recursive: true, force: true })
  process.exit(1)
}

fs.mkdirSync(path.dirname(output), { recursive: true })
fs.copyFileSync(path.join(sceneDir, rendered), output)
fs.rmSync(mediaDir, { recursive: true, force: true })
console.log('Rendered ' + output)
