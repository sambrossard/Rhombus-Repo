### Documentation for `##Console Clean` Script

---

#### Overview

The `##Console Clean` script is designed to interact with Rhombus Systems' API to manage and clean up various policies, roles, schedules, and other entities such as camera policies, sensor policies, door policies, and more. The script provides functionality to retrieve, filter, and delete these entities based on specific criteria, such as their names containing the word "demo".

---

### Dependencies

This script requires the following dependencies:

- **Python 3.x**
- **Requests Library**: Used for making HTTP requests to the Rhombus Systems API. Install it using `pip install requests`.
- **Pprint Library**: Used for pretty-printing JSON data. This is a standard library in Python.

---

### Classes and Methods

#### `CameraPolicies`
This class handles operations related to camera policies, sensor policies, door policies, and related entities.

- **`get_camera_policies(self)`**: Retrieves camera policies from the API.
- **`get_sensor_policy(self)`**: Retrieves sensor policies from the API.
- **`get_sensor_door_policy(self)`**: Retrieves door sensor policies from the API.
- **`get_video_intercome_policy(self)`**: Retrieves video intercom policies from the API.
- **`get_door_policy(self)`**: Retrieves access-controlled door policies from the API.
- **`get_audio_policy(self)`**: Retrieves audio policies from the API.
- **`get_motion_policy(self)`**: Retrieves occupancy (motion detection) policies from the API.

Each of the above methods makes a POST request to the Rhombus Systems API and returns the JSON response.

- **Filtering Methods**: Each entity has a corresponding filter method, such as `filter_audio_policy`, `filter_door_policy`, etc., which filters the retrieved data based on specific criteria (e.g., name contains "demo").

- **Deletion Methods**: Methods such as `delete_policies`, `delete_sensor_policy`, etc., use the filtered data to delete the corresponding entities via the API.

#### `SharedStreams`
This class handles operations related to shared video streams.

- **`find_shared_streams(self)`**: Retrieves all shared live video streams.
- **`filter_shared_streams(self, live_data)`**: Filters shared streams whose names contain "demo".
- **`delete_shared_streams(self)`**: Deletes filtered shared streams.

#### `GetVideoWall`
This class manages video walls.

- **`get_video(self)`**: Retrieves video walls from the API.
- **`filter_wall(self, wall_json)`**: Filters video walls whose names contain "demo".
- **`delete_video_walls(self)`**: Deletes filtered video walls.

#### `GetRole`
This class handles operations related to permission groups (roles).

- **`get_roles(self)`**: Retrieves permission groups from the API.
- **`filter_roles(self, role_data)`**: Filters roles whose names contain "demo".
- **`delete_permission_group(self)`**: Deletes filtered roles.

#### `Schedules`
This class manages schedules.

- **`get_schedules(self)`**: Retrieves schedules from the API.
- **`filter_schedules(self, schedule_response)`**: Filters schedules whose names contain "demo".
- **`delete_schedule(self)`**: Deletes filtered schedules.

#### `AccessGrants`
This class handles access grants.

- **`find_grants_by_org(self)`**: Retrieves access grants by organization.
- **`filter_grants(self, grant_json)`**: Filters access grants whose names contain "demo".
- **`delete_grants(self)`**: Deletes filtered access grants.

### `run_cleanse()` Function

The `run_cleanse` function is the main entry point of the script. It instantiates the various classes and invokes their methods to clean up entities that meet specific criteria. The function is designed to be run in sequence to delete all demo-related policies, roles, streams, and schedules.

### Usage

To run the script, simply execute it with Python:

```bash
python console_clean.py