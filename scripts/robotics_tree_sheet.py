#!/usr/bin/env python3
"""Native 16 px robotics hierarchies, mixing new and reused semantic symbols.

These are cross-application integration examples, not executable robot programs
or a claim about any vendor's exact UI. Alternative joint types form a library.
"""
import json, re
from html import escape
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ICONS={i['id']:i for i in json.loads((ROOT/'manifest.json').read_text())['icons']}
TREES=[('Cell and program instructions',[
 (0,'olp-robot-cell','Offline workcell'),
 (1,'olp-robot-controller','Controller configuration'),
 (1,'olp-robot-arm','Robot model'),
 (2,'cad-part','Base link [shared part SVG]'),
 (2,'cad-revolute-joint','Shoulder joint'),
 (2,'olp-end-effector','Gripper / end-effector group'),
 (3,'olp-payload','Tool and carried load'),
 (3,'olp-force-torque-sensor','Wrist force-torque sensor'),
 (1,'olp-reference-frame','Work frame'),
 (1,'olp-generate-program','Handling program'),
 (2,'olp-set-speed','Motion speed'),
 (2,'olp-path-blend','Path blend'),
 (2,'olp-program-if','Conditional branch'),
 (3,'olp-wait-signal','Input condition wait'),
 (3,'olp-program-wait','Timed wait'),
 (2,'olp-program-loop','Repeat block'),
 (3,'olp-attach-object','Attachment event'),
 (3,'olp-linear-move','Linear move'),
 (3,'olp-detach-object','Release event'),
 (2,'olp-program-thread','Concurrent task'),
 (3,'olp-digital-output','Digital output'),
 (2,'olp-task-synchronization','Task synchronization'),
 (2,'olp-operator-message','Operator message'),
]),('Robot model and motion planning',[
 (0,'cad-assembly','Kinematic model'),
 (1,'cad-planar-joint','Mobile-root planar joint'),
 (1,'cad-part','Chassis link'),
 (2,'cad-mass-properties','Mass and inertia'),
 (2,'cad-mesh-body','Visual mesh'),
 (2,'cad-mesh-body','Collision mesh [same SVG]'),
 (1,'cad-fixed-joint','Fixed sensor mount'),
 (1,'olp-camera-sensor','Depth camera'),
 (1,'cmm-laser-scanner','LiDAR [shared scanner SVG]'),
 (1,'olp-imu-sensor','Inertial sensor'),
 (0,'olp-planning-group','Arm planning group'),
 (1,'olp-joint-target','Named home pose'),
 (1,'olp-end-effector','End-effector group'),
 (0,'olp-collision-matrix','Collision pair matrix'),
 (0,'olp-motion-constraints','Path orientation constraint'),
 (0,'olp-occupancy-map','Occupancy map'),
 (0,'cae-solver-settings','Physics settings'),
 (0,'cae-contact-pair','Physical contact definition'),
 (0,'common-folder','Alternative joint library'),
 (1,'cad-ball-joint','Ball joint'),
 (1,'cad-floating-joint','Floating joint'),
 (1,'cad-screw-joint','Screw joint'),
 (1,'cad-universal-joint','Universal joint'),
 (1,'cad-joint-coupling','Mimic / joint coupling'),
]),('Process and station logic',[
 (0,'common-folder','Offline process definitions'),
 (1,'olp-generate-program','Process program'),
 (2,'olp-palletizing','Palletizing sequence'),
 (2,'olp-conveyor-tracking','Conveyor-tracking block'),
 (2,'olp-force-control','Force-control block'),
 (3,'olp-tool-contact','Contact-search motion'),
 (2,'olp-remote-tcp','Stationary-tool motion'),
 (2,'olp-point-follow','Point-follow project'),
 (2,'olp-weld-weave','Weld weave'),
 (1,'olp-safety-zone','Modeled workspace boundary'),
 (1,'olp-swept-volume','Recorded motion envelope'),
 (0,'common-folder','Station logic and observations'),
 (1,'olp-io-mapping','Sensor-to-controller I/O mapping'),
 (1,'olp-signal-analyzer','Recorded signal trace'),
 (1,'olp-program-event','Input event handler'),
 (2,'olp-variable-assignment','Counter assignment'),
 (2,'olp-script-instruction','Custom script instruction'),
 (1,'olp-tool-frame','Active tool-frame instruction'),
 (0,'common-folder','Repeated object instances'),
 (1,'cad-part','Fixture:1 [same part SVG]'),
 (1,'cad-part','Fixture:2 [same part SVG]'),
 (1,'olp-cartesian-target','Approach target'),
 (1,'olp-cartesian-target','Retract target [same SVG]'),
])]
width=1320;panelheight=64+max(len(r) for _,r in TREES)*24;height=panelheight+145
parts=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}"><rect width="{width}" height="{height}" fill="#f4f7f5"/><text x="24" y="34" font-family="sans-serif" font-size="22" fill="#253b53">CAX / robotics model trees and program instructions</text><text x="24" y="59" font-family="sans-serif" font-size="12" fill="#526f68">Native 16 px symbols · 24 px rows · new commands and existing objects share their SVGs · illustrative hierarchy</text>']
for col,(title,rows) in enumerate(TREES):
 x=18+col*435
 parts.append(f'<rect x="{x}" y="80" width="422" height="{panelheight}" rx="9" fill="white" stroke="#d8e2dc"/><text x="{x+14}" y="108" font-family="sans-serif" font-size="15" fill="#253b53">{escape(title)}</text>')
 for n,(depth,id,label) in enumerate(rows):
  i=ICONS[id];y=127+n*24;ix=x+15+depth*17
  assert 'model-tree' in i['usages'],id
  if n%2:parts.append(f'<rect x="{x+1}" y="{y-3}" width="420" height="24" fill="#f7f9f7"/>')
  if depth:parts.append(f'<path d="M{ix-10} {y-4} V{y+8} H{ix-4}" stroke="#c4d1cb" fill="none"/>')
  prefix=f'robot-tree-{col}-{n}-'
  body=re.sub(r'id="([^"]+)"',lambda m:f'id="{prefix}{m[1]}"',i['body'])
  body=re.sub(r'url\(#([^)]+)\)',lambda m:f'url(#{prefix}{m[1]})',body)
  parts.append(f'<svg x="{ix}" y="{y}" width="16" height="16" viewBox="0 0 32 32" fill="none" stroke="#253b53" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">{body}</svg><text x="{ix+23}" y="{y+12}" font-family="sans-serif" font-size="12" fill="#253b53">{escape(label)}</text>')
parts.append(f'<text x="24" y="{height-35}" font-family="sans-serif" font-size="12" fill="#526f68">Visual and collision meshes, gripper instances and robot morphologies reuse symbols. Joint types express different degrees of freedom.</text><text x="24" y="{height-15}" font-family="sans-serif" font-size="11" fill="#526f68">Cross-application examples only. Not runnable robot logic, an exact vendor UI, certified safety boundaries or a live controller connection.</text></svg>')
(ROOT/'qa/robotics-model-tree.svg').write_text(''.join(parts))
print(f'Built robotics hierarchy with {sum(len(r) for _,r in TREES)} native 16px rows')
