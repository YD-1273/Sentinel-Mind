## Week 1

### [8/25/2026, 3:10 AM]
**Phase:** 1 — Environment Setup & Core Vision Pipeline

**Done:**
- Set up WSL2 + Python 3.12 venv
- Installed torch (CUDA), opencv-python, ultralytics, deepface
- Git repo initialized, connected to GitHub (YD-1273/Sentinel-Mind)
- Fixed GitHub push auth issue (switched to Personal Access Token, resolved 403 by regenerating token with correct `repo` scope)
- Set up usbipd-win for webcam passthrough from Windows to WSL
- Wrote YOLOv8 person detection script (`src/detection/detect.py`)
- Debugged webcam capture issues in WSL:
  - `cv2.imshow()` failed (no display server in WSL) → switched to writing annotated frames to `output.mp4` instead of live preview
  - First output.mp4 was empty → fixed by reading actual frame width/height from capture instead of hardcoding
  - Output was single-frame (not video) → root cause was slow `cap.read()` at 1920x1080 over USB passthrough (~15+ sec/frame)
  - Fixed by forcing capture resolution down to 640x480 — frame reads became fast and stable
- Confirmed: YOLOv8 successfully detects `person` class on live webcam feed via WSL, captured 100 frames cleanly

**Issues hit:**
- GitHub auth (password deprecated) — resolved via PAT
- usbipd PATH not recognized right after install — resolved by reopening terminal
- WSL GUI display not available for `cv2.imshow()` — bypassed by saving to video file
- High-res webcam capture too slow over WSL USB passthrough — resolved by lowering capture resolution

**Next:**
- Integrate DeepFace on detected person crops
- Build small authorized-faces folder + compute embeddings
- Implement Authorized/Unknown matching logic

---
