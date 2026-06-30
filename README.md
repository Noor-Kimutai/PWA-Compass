# Scavenger Hunt PWA Compass

A high-performance, single-file Progressive Web Application (PWA) designed for real-world urban adventure games.

This application functions under a **Zero Physical Inventory Model** and strips away traditional map visual assets and cardinal directions, guiding players using only a dynamic mechanical vector pointer and a raw digital distance readout.

## Features

- **Pure Night Mode Aesthetic:** Stark high-contrast `#FFFFFF` active elements and text over a `#000000` pitch-black background. Warning states are displayed in solid `#FF0000` red.
- **Geofence Lockout Gate:** Automatically locks and disables the seed phrase input block if the player is $> 15$ meters away from the active checkpoint target, displaying: *"KEEP WALKING. YOU ARE TOO FAR TO SPEAK TO THIS CHARACTER."*
- **Auto-Sanitized Cryptographic Unlocking:** Automatically sanitizes spacing and handles uppercase text input before matching 12-word seed phrases to unlock subsequent navigation coordinates.
- **Sensor Calibration Math:** Calculated locally on client hardware:
  - **Distance:** Earth's surface calculations using the Haversine equation.
  - **Bearing:** Target angle calculations using the azimuth math.
  - **Compass Needle:** Shortest-path rotation angles mapped to device compass APIs (with Android `deviceorientationabsolute` and iOS `webkitCompassHeading` fallbacks).
- **Built-in Developer Simulation Dashboard:** Collapsible drawer featuring mock sensor triggers, heading sliders, and latitude/longitude inputs to test waypoint locks.
- **Compact Offline Support:** Self-contained inline Web App Manifest and dynamic Blob-registered Service Worker configuration to support "Add to Home Screen" standalone installations.

## Mock Coordinates Database

The application comes preconfigured with the following local testing milestones:
1. **START GATE (Default):** Latitude `0.5142`, Longitude `35.2697` (Zion Mall, Eldoret)
2. **WAYPOINT 1 (Unlock Key):** `ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT GOLF HOTEL INDIA JULIET KILO LIMA` -> Coordinates `0.5212`, `35.2601`
3. **WAYPOINT 2 (Unlock Key):** `ONE TWO THREE FOUR FIVE SIX SEVEN EIGHT NINE TEN ELEVEN TWELVE` -> Coordinates `0.5115`, `35.2814`

## How to Run & Deploy

Since the entire application is fully contained in a single file (`index.html`), it requires zero compilation or complex hosting setup.

### Local Development / Mobile Testing
To run the server and test mobile sensors:
1. Run a local web server (e.g. via Python) inside this folder:
   ```bash
   python -m http.server 8000 --bind 0.0.0.0
   ```
2. Find your computer's local IP address (using `ipconfig` on Windows or `ifconfig` on macOS/Linux).
3. Open a browser on your Android/iOS phone and navigate to `http://<your-computer-ip>:8000`.
4. **Sensor Permissions Bypass (Insecure Origin):**
   Modern mobile browsers restrict GPS/Compass orientation access to HTTPS connections. To bypass this locally on Google Chrome (Android):
   - Go to `chrome://flags/#unsafely-treat-insecure-origin-as-secure` on your phone's Chrome browser.
   - Enable the flag and add your local URL: `http://<your-computer-ip>:8000`.
   - Relaunch Chrome. The app will have full access to GPS and orientation compass sensors!
