##Console Clean
import requests
import pprint 


##getCameraPolicies
class CameraPolicies:

    def get_camera_policies(self):

        url = "https://api2.rhombussystems.com/api/policy/getCameraPolicies"

        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            # pprint.pprint(data)
            return data
        else:
            print(f'Request Failed with Status Code {response.status_code}')
            
    
    def get_sensor_policy(self):
        
        url = "https://api2.rhombussystems.com/api/policy/getClimatePolicies"

        payload = { "newKey": "New Value" }
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
    }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            sensor_data = response.json()
            # pprint.pprint(sensor_data)
            return sensor_data
        else:
            print(f'Request failed with status code {response.status_code}')

    
    def get_sensor_door_policy(self):

        url = "https://api2.rhombussystems.com/api/policy/getDoorPolicies"

        payload = { "newKey": "New Value" }
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
}

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            door_data = response.json()
            # pprint.pprint(door_data)
            return door_data
        else:
            print(f'Request failed with status code {response.status_code}')


    def get_video_intercome_policy(self):

        url = "https://api2.rhombussystems.com/api/policy/getVideoIntercomPolicies"

        payload = { "newKey": "New Value" }
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
}

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            intercom_data = response.json()
            # pprint.pprint(intercom_data)
            return intercom_data
        else:
            print(f'Request failed with status code {response.status_code}')


    def get_door_policy(self):
        url = "https://api2.rhombussystems.com/api/policy/getAccessControlledDoorPolicies"

        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
    }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            door_policy_data = response.json()
            # pprint.pprint(door_policy_data)
            return door_policy_data
        else:
            print(f'Request failed with status code {response.status_code}')


    def get_audio_policy(self):
        url = "https://api2.rhombussystems.com/api/policy/getAudioPolicies"

        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            audio_data = response.json()
            # pprint.pprint(audio_data)
            return(audio_data)
        else:
            print(f'Request failed with status code {response.status_code}')


    def get_motion_policy(self):

        url = "https://api2.rhombussystems.com/api/policy/getOccupancyPolicies"

        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            motion_data = response.json()
            # pprint.pprint(motion_data)
            return motion_data
        else:
            print(f'Request failed with status code {response.status_code}')


    def filter_audio_policy(self, audio_data): ##GOOD
        audio_uuid = []
        nested_audio_uuid = audio_data.get("policies", [])
        for policy in nested_audio_uuid:
            name = policy.get("name").lower()
            if "demo" in name:
                audio_uuid.append(policy.get("uuid"))
        if audio_uuid:
            pprint.pprint(f'Audio Policy uuid {audio_uuid}')
            return audio_uuid
        else:
            print('No audio policies to delete')
            return None


    def filter_door_policy(self, door_policy_data): ##GOOD
        door_uuid = []
        nested_door_uuid = door_policy_data.get("policies", [])
        for policy in nested_door_uuid:
            name = policy.get("name").lower()
            if "demo" in name:
                door_uuid.append(policy.get("uuid"))
        if door_uuid:
            pprint.pprint(f'Door Policy uuid {door_uuid}')
            return door_uuid
        else:
            print('No door policies to delete')
            return None


    def filter_intercom(self, intercom_data): ##GOOD
        video_intercom_dump = []
        nested_intercom_data = intercom_data.get("policies", [])
        for policy in nested_intercom_data:
            name = policy.get("name").lower()
            if 'demo' in name:
                video_intercom_dump.append(policy.get('uuid'))
        if video_intercom_dump:
            pprint.pprint(f'Intercom Policy uuid {video_intercom_dump}')
            return video_intercom_dump
        else:
            print('No intercom policies to delete')
            return None


    def filter_door_sensor_policy(self, door_data): ##GOOD
        door_dump = []
        nested_door_data = door_data.get("policies", [])
        for policy in nested_door_data:
            name = policy.get("name").lower()
            if 'demo' in name:
                door_dump.append(policy.get("uuid"))
        if door_dump:
            pprint.pprint(f'Door Sensor Policy uuid {door_dump}')
            return door_dump
        else:
            print('No door sensor policies to delete')
            return None


    def filter_sensor_data(self, sensor_data): ##GOOD
        sensor_data_dump = []
        nested_sensor_data = sensor_data.get("policies", [])
        for policy in nested_sensor_data:
            name = policy.get('name').lower()
            if 'demo' in name:
                sensor_data_dump.append(policy.get('uuid'))
        if sensor_data_dump:
            pprint.pprint(f'Sensor Policy uuid {sensor_data_dump}')
            return sensor_data_dump
        else:
            print('No policies to delete')
            return None
        

    def filter_camera_data(self, data): ##GOOD
        filtered_data = []
        nested_policy = data.get("policies", [])
        for policy in nested_policy:
            name = policy.get("name").lower()
            if "demo" in name:
                filtered_data.append(policy.get('uuid'))
        if filtered_data:
            pprint.pprint(f'Camera Policy uuid: {filtered_data}')
            return filtered_data
        else:
            print('No camera policies found')
            return None
    
    
    def filter_motion_data(self, motion_data): ##GOOD
        filtered_data = []
        nested_uuid = motion_data.get("policies", [])
        for policy in nested_uuid:
            name = policy.get("name").lower()
            if "demo" in name:
                filtered_data.append(policy.get("uuid"))
        if filtered_data:
            pprint.pprint(f'Motion Policy uuid: {filtered_data}')
            return filtered_data
        else:
            print('No motion policies to delete')
            return None
    

    #deleteCameraPolicies
    def delete_policies(self):
        filtered_json = self.get_camera_policies()
        if not filtered_json:
            print('No get response')
            return
        filtered_data = self.filter_camera_data(filtered_json)

        if not filtered_data:
            print('No camera policies to delete')
            return

        for uuid in filtered_data:
            payload = {
                'policyUuid': uuid
                }

            url = "https://api2.rhombussystems.com/api/policy/deleteCameraPolicy"
            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
            }
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Policy with UUID {uuid} deleted successfully')
            else:
                print(f'Request failed with status code {response.status_code}')


    def delete_sensor_policy(self):
        sensor_data = self.get_sensor_policy()
        if not sensor_data:
            print('No get response')
            return
        sensor_data_dump = self.filter_sensor_data(sensor_data)

        if not sensor_data_dump:
            print("No sensor Policies to delete")
            return
        
        for uuid in sensor_data_dump:
            payload = { 
                "policyUuid": uuid 
            }
            url = "https://api2.rhombussystems.com/api/policy/deleteClimatePolicy"

            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
            }
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                pprint.pprint(f'sensor policy with uuid {uuid} deleted')
                
            else:
                print(f'Request failed with status code {response.status_code}')

    def delete_door_sensor_policy(self):
        door_data = self.get_sensor_door_policy()
        if not door_data:
            print('no get response')
            return
        door_dump = self.filter_door_sensor_policy(door_data)

        if not door_dump:
            print('No door sensor policies to delete')
            return

        for uuid in door_dump:

            url = "https://api2.rhombussystems.com/api/policy/deleteDoorPolicy"

            payload = { 
                "policyUuid": uuid
                        }
            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
}

            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Policy with uuid {uuid} deleted')
            else:
                print(f'Request failed with status code {response.status_code}')
    
    def delete_intercom_policy(self): 
        video_intercom_data = self.get_video_intercome_policy()
        if not video_intercom_data:
            print('No policies to delete')
            return
        video_intercom_dump = self.filter_intercom(video_intercom_data)

        if not video_intercom_dump:
            print('No intercom policies to delete')
            return

        for uuid in video_intercom_dump:

            url = "https://api2.rhombussystems.com/api/policy/deleteVideoIntercomPolicy"

            payload = { 
                "policyUuid": uuid 
                }
            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
}

            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Policies with uuid {uuid} deleted')
            else:
                print(f'Request failed with status code {response.status_code}')
    
    def delete_door_policy(self):
        door_policy = self.get_door_policy()
        if not door_policy:
            print("No policies to delete")
            return
        door_uuid = self.filter_door_policy(door_policy)

        if not door_uuid:
            print('No door policies to delete')
            return

        for uuid in door_uuid:

            url = "https://api2.rhombussystems.com/api/policy/deleteAccessControlledDoorPolicy"

            payload = { 
                "policyUuid": uuid 
                }
            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
}

            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Policy with uuid {uuid} deleted')
            else:
                print(f'Request failed with status code {response.status_code}')
    
    def delete_audio_policy(self):
        audio_policy = self.get_audio_policy()
        if not audio_policy:
            print("No policies to delete")
            return
        audio_uuid = self.filter_audio_policy(audio_policy)

        if not audio_uuid:
            print('No audio policies to delete')
            return

        for uuid in audio_uuid:

            url = "https://api2.rhombussystems.com/api/policy/deleteAudioPolicy"

            payload = { 
                "policyUuid": uuid
                }
            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
            }

            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Policy with uuid {uuid} deleted')
            else:
                print(f'Request failed withs status code {response.status_code}')

    def delete_motion_policy(self):
        motion_policy = self.get_motion_policy()
        if not motion_policy:
            print("no policy to delete")
            return
        filtered_data = self.filter_motion_data(motion_policy)

        if not filtered_data:
            print('No motion policies to delete')
            return

        for uuid in filtered_data:

            url = "https://api2.rhombussystems.com/api/policy/deleteOccupancyPolicy"

            payload = { 
                "policyUuid": uuid
                }
            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
            }

            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f"Policy uuid {uuid} deleted")
            else:
                print(f'Request failed with status code {response.status_code}')



##findAllSharedLiveVideoStreams


class SharedStreams:

    def find_shared_streams(self):
        url = "https://api2.rhombussystems.com/api/camera/findAllSharedLiveVideoStreams"

        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            live_data = response.json()
            # pprint.pprint(live_data)
            return live_data
        else:
            print(f'Request Failed with status code {response.status_code}')
            return None


    def filter_shared_streams(self, live_data): #GOOD
        live_data_filter = []
        nested_stream = live_data.get("sharedLiveVideoStreams", [])
        for stream in nested_stream:
            name = stream.get("name")
            if name and "demo" in name.lower():
                live_data_filter.append({
                    'cameraUuid': stream.get('cameraUuid'),
                    'uuid': stream.get('uuid')
                })
        if live_data_filter:
            pprint.pprint(f'Stream Policy uuid {live_data_filter}')
            return live_data_filter
        else:
            print("no streams to delete")
            return None
    


    def delete_shared_streams(self):
        live_data = self.find_shared_streams()
        if not live_data:
            print('No Un-named streams')
            return

        live_data_filter = self.filter_shared_streams(live_data)  

        if not live_data_filter:
            print('No streams to delete')
            return

        for stream in live_data_filter:
            payload = {  
                'cameraUuid': stream['cameraUuid'],
                'uuid': stream['uuid']
            }

            url = "https://api2.rhombussystems.com/api/camera/deleteSharedLiveVideoStream"

            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
            }

            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Stream with UUID {stream["uuid"]} deleted successfully')
            else:
                print(f'Request failed with status code {response.status_code}')


## getVideoWall
class GetVideoWall:

    def get_video(self):

        url = "https://api2.rhombussystems.com/api/camera/getVideoWalls"

        payload = { "newKey": "New Value" }
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            wall_json = response.json()
            # pprint.pprint(wall_json)
            return wall_json
        else:
            print(f'Request failed with status code {response.status_code}')


    def filter_wall(self, wall_json): 
        uuid_dump = []
        video_walls = wall_json.get("videoWalls", [])
        for wall in video_walls:
            name = wall.get("displayName").lower()
            if "demo" in name:
                uuid_dump.append(wall.get("uuid"))
        if uuid_dump:
            pprint.pprint(f' Videowall uuid: {uuid_dump}')
            return uuid_dump
        else:
            print('No video walls to delete')
            return None
    

    def delete_video_walls(self):
        delete_walls = self.get_video()
        if not delete_walls:
            print('No walls to delete')
            return
        uuid_dump = self.filter_wall(delete_walls)

        if not uuid_dump:
            print('No video walls to delete')
            return

        for uuid in uuid_dump:

            url = "https://api2.rhombussystems.com/api/camera/deleteVideoWall"

            payload = { 
                "uuid": uuid 
                }
            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
}
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Video Wall with uuid {uuid} deleted successfully')
            else:
                print('No video walls to delete')


class GetRole:

    def get_roles(self):
        
        url = "https://api2.rhombussystems.com/api/permission/getPermissionGroups"

        headers = {
        "accept": "application/json",
        "x-auth-scheme": "api-token",
        "content-type": "application/json",
        "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
    }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            role_data = response.json()
            # pprint.pprint(role_data)
            return role_data
        else:
            print(f'Request failed with status code {response.status_code}')


    def filter_roles(self, role_data):
        role_dump = []
        grab_role = role_data.get('permissionGroups', [])
        for id in grab_role:
            name = id.get("name").lower()
            if "demo" in name:
                role_dump.append(id.get('uuid'))
        if role_dump:
            pprint.pprint(f' Role uuid: {role_dump}')
            return role_dump
        else:
            print("No roles to delete")
            return None 
    

    def delete_permission_group(self):
        final_role = self.get_roles()
        if not final_role:
            print('no roles to delete')
            return
        role_dump = self.filter_roles(final_role)

        if not role_dump:
            print('No roles to delete')
            return
        
        for uuid in role_dump:
            payload = { 
                "groupUuid": uuid
        }
            url = "https://api2.rhombussystems.com/api/permission/deletePermissionGroup"


            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f' roles deleted with uuid {uuid}')
            else:
                print(f'request failed with status code {response.status_code}')


class Schedules:

    def get_schedules(self):
        url = "https://api2.rhombussystems.com/api/schedule/getSchedules"

        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

        response = requests.post(url, headers=headers)
        if response.status_code == 200:
            schedule_response = response.json()
            # pprint.pprint(schedule_response)
            return schedule_response
        else:
            print(f'Request failed with status code {response.status_code}')
            return None


    def filter_schedules(self, schedule_response):
        schedule_dump = []
        weekly_schedules = schedule_response.get('weeklySchedules', [])
        for schedule in weekly_schedules:
            name = schedule.get("name").lower()
            if "demo" in name:
                schedule_dump.append(schedule.get('uuid'))
        if schedule_dump:
            pprint.pprint(f'Schedule uuid: {schedule_dump}')
            return schedule_dump
        else:
            print('No schedules to delete')
            return None


    def delete_schedule(self):
        remove_schedule = self.get_schedules()
        if not remove_schedule:
            print('no schedules to delete')
            return
        schedule_dump = self.filter_schedules(remove_schedule)

        if not schedule_dump:
            print('No schedules to delete')
            return
        
        for schedule in schedule_dump:
                
            payload = { 
                "scheduleUuid": schedule 
                }
            url = "https://api2.rhombussystems.com/api/policy/deleteSchedule"

            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Schedules with uuid {schedule} deleted')
                return
            else:
                print(f'Request failed with status code {response.status_code}')


class AccessGrants:

    def find_grants_by_org(self):

        url = "https://api2.rhombussystems.com/api/accesscontrol/findLocationAccessGrantsByOrg"

        payload = {"newKey": ""}
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ" 
    }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            grant_json = response.json()
            # pprint.pprint(grant_json)
            return grant_json
        else:
            print(f'Request failed with status code {response.status_code}')


    def filter_grants(self, grant_json):
        grant_uuids = []
        grant_groups = grant_json.get("accessGrants", [])
        for groups in grant_groups:
            if 'sam' in groups.get('name').lower():
                grant_uuids.append(groups.get('uuid'))
        if grant_uuids:
            pprint.pprint(f'Access Grant uuids: {grant_uuids}')
            return grant_uuids
        else:
            print('no access grants to delete')
            return None
    

    def delete_grants(self): 
        remove_grants = self.find_grants_by_org()
        if not remove_grants:
            print('No grants to remove')
            return
        grant_uuids = self.filter_grants(remove_grants)

        if not grant_uuids:
            print('No grants to delete')
            return

        for uuid in grant_uuids:

            payload = { 
                "accessGrantUuid": uuid 
            }

            url = "https://api2.rhombussystems.com/api/accesscontrol/deleteLocationAccessGrant"

            
            headers = {
                "accept": "application/json",
                "x-auth-scheme": "api-token",
                "content-type": "application/json",
                "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }
        
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                pprint.pprint(f'Grants with uuid {uuid} deleted successfully')
            else:
                print(f'Request failed with status code {response.status_code}')



def run_cleanse():

    camera_policies_instance = CameraPolicies()

    get_camera = camera_policies_instance.get_camera_policies()
    camera_policies_instance.filter_camera_data(get_camera)
    camera_policies_instance.delete_policies()

    sensor_policy = camera_policies_instance.get_sensor_policy()
    camera_policies_instance.filter_sensor_data(sensor_policy)
    camera_policies_instance.delete_sensor_policy()

    door_sensor_policy = camera_policies_instance.get_sensor_door_policy()
    camera_policies_instance.filter_door_sensor_policy(door_sensor_policy)
    camera_policies_instance.delete_door_sensor_policy()

    get_intercom = camera_policies_instance.get_video_intercome_policy()
    camera_policies_instance.filter_intercom(get_intercom)
    camera_policies_instance.delete_intercom_policy()

    get_door = camera_policies_instance.get_door_policy()
    camera_policies_instance.filter_door_policy(get_door)
    camera_policies_instance.delete_door_policy()

    get_audio = camera_policies_instance.get_audio_policy()
    camera_policies_instance.filter_audio_policy(get_audio)
    camera_policies_instance.delete_audio_policy()

    get_motion = camera_policies_instance.get_motion_policy()
    camera_policies_instance.filter_motion_data(get_motion)
    camera_policies_instance.delete_motion_policy()


    solution = SharedStreams()
    live_data =  solution.find_shared_streams()
    solution.filter_shared_streams(live_data)
    solution.delete_shared_streams()

    get_walls = GetVideoWall()
    video_data = get_walls.get_video()
    get_walls.filter_wall(video_data)
    get_walls.delete_video_walls() 

    permission_groups = GetRole()
    role_data = permission_groups.get_roles()
    permission_groups.filter_roles(role_data) 
    permission_groups.delete_permission_group()

    schedule_list = Schedules()
    find_schedule = schedule_list.get_schedules()
    schedule_list.filter_schedules(find_schedule)
    schedule_list.delete_schedule()

    get_grants = AccessGrants()
    grant_response = get_grants.find_grants_by_org()
    get_grants.filter_grants(grant_response)
    get_grants.delete_grants()


if __name__ == '__main__':
    run_cleanse()



    






