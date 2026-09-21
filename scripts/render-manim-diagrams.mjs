import { spawnSync } from 'node:child_process'
import fs from 'node:fs'
import os from 'node:os'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..')
const manimDir = path.join(root, 'docs', 'manim')
const manim = path.join(root, '.manim-venv', 'bin', 'manim')

const diagrams = [
  {
    source: 'tidal_convergence.py',
    scene: 'TidalConvergence',
    output: 'tidal-convergence.png',
    page: 'equivalence-principle',
  },
  {
    source: 'light_bending_in_lift.py',
    scene: 'LightBendingInLift',
    output: 'light-bending-in-lift.png',
    page: 'equivalence-principle',
  },
  {
    source: 'intrinsic_flatness.py',
    scene: 'IntrinsicFlatness',
    output: 'intrinsic-flatness.png',
    page: 'tensors-and-tensor-fields',
  },
  {
    source: 'parallel_transport_sphere.py',
    scene: 'ParallelTransportSphere',
    output: 'parallel-transport-sphere.png',
    page: 'tensors-and-tensor-fields',
  },
  {
    source: 'tangent_spaces.py',
    scene: 'TangentSpaces',
    output: 'tangent-spaces.png',
    page: 'tensors-and-tensor-fields',
  },
  {
    source: 'contravariant_rescaling.py',
    scene: 'ContravariantRescaling',
    output: 'contravariant-rescaling.png',
    page: 'tensors-and-tensor-fields',
  },
  {
    source: 'gradient_form.py',
    scene: 'GradientForm',
    output: 'gradient-form.png',
    page: 'tensors-and-tensor-fields',
  },
  {
    source: 'gradient_curved_surface.py',
    scene: 'GradientCurvedSurface',
    output: 'gradient-curved-surface.png',
    page: 'tensors-and-tensor-fields',
  },
  {
    source: 'one_form_measuring_tape.py',
    scene: 'OneFormMeasuringTape',
    output: 'one-form-measuring-tape.png',
    page: 'tensors-and-tensor-fields',
  },
  {
    source: 'covariant_measuring_tape.py',
    scene: 'CovariantMeasuringTape',
    output: 'covariant-measuring-tape.png',
    page: 'tensors-and-tensor-fields',
  },
  {
    source: 'product_rule_decomposition.py',
    scene: 'ProductRuleDecomposition',
    output: 'product-rule-decomposition.png',
    page: 'spacetime',
  },
  {
    source: 'connection_indices.py',
    scene: 'ConnectionIndices',
    output: 'connection-indices.png',
    page: 'spacetime',
  },
  {
    source: 'connection_indices_3d.py',
    scene: 'ConnectionIndices3D',
    output: 'connection-indices-3d.png',
    page: 'spacetime',
  },
]

const args = process.argv.slice(2)
if (args.length && (args.length !== 2 || args[0] !== '--page')) {
  console.error('Usage: pnpm docs:manim [--page <chapter-slug>]')
  process.exit(1)
}

const selected = args.length ? diagrams.filter((diagram) => diagram.page === args[1]) : diagrams
if (!selected.length) {
  console.error(`No diagrams registered for page: ${args[1]}`)
  process.exit(1)
}

if (!fs.existsSync(manim)) {
  console.error(`Manim not found at ${manim}`)
  console.error('Create it with: uv venv .manim-venv --python 3.14 && uv pip install --python .manim-venv/bin/python manim')
  process.exit(1)
}

const mediaDir = fs.mkdtempSync(path.join(os.tmpdir(), 'gr-manim-'))
let renderedCount = 0
let failedCount = 0

for (const { source, scene, output } of selected) {
  const result = spawnSync(
    manim,
    [
      'render',
      '-s',
      '--tex_template',
      path.join(manimDir, 'template.tex'),
      '--media_dir',
      mediaDir,
      '-r',
      '2400,1350',
      '-q',
      'm',
      path.join('docs', 'manim', source),
      scene,
    ],
    { cwd: root, stdio: 'pipe', encoding: 'utf8' },
  )

  if (result.status !== 0) {
    failedCount++
    console.error(`FAIL ${source}\n${result.stderr || result.stdout}`)
    continue
  }

  const imagesDir = path.join(mediaDir, 'images', path.basename(source, '.py'))
  const rendered = fs.readdirSync(imagesDir).find(
    (file) => file.startsWith(`${scene}_ManimCE_v`) && file.endsWith('.png'),
  )
  if (!rendered) {
    failedCount++
    console.error(`FAIL ${source}: no rendered PNG found in ${imagesDir}`)
    continue
  }

  fs.copyFileSync(path.join(imagesDir, rendered), path.join(manimDir, output))
  renderedCount++
  console.log(`ok   ${source} -> docs/manim/${output}`)
}

fs.rmSync(mediaDir, { recursive: true, force: true })
console.log(`\n${renderedCount} diagram(s) rendered, ${failedCount} failed.`)

if (failedCount > 0) process.exitCode = 1
