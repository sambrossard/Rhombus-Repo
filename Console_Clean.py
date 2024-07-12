##Console Clean
import requests
import pprint 


##getCameraPolicies
class CameraPolicies:

    def camera_policies(self):
        url = "https://api2.rhombussystems.com/api/policy/getCameraPolicies"

        payload = { 
            "newKey": "New Value",
            'policyUuid': '' 
        }
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return self.filter_data(data)
        else:
            print(f'Request Failed with Status Code {response.status_code}')
            return []

    def filter_data(self, data):
        filtered_data = []
        if "policies" in data:
            for policy in data["policies"]:
                name = policy.get('name', '').lower()
                if 'test' in name or 'after hours' in name:
                    filtered_data.append(policy['uuid'])
        pprint.pprint(filtered_data)
        return filtered_data
        
    #deleteCameraPolicies
    def delete_policies(self):
        filtered_data = self.camera_policies()
        if not filtered_data:
            print('no policies to delete')

        url = "https://api2.rhombussystems.com/api/policy/deleteCameraPolicy"
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }
        for uuid in filtered_data:
            payload = {'policyUuid': uuid}
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Policy with UUID {uuid} deleted successfully')
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
            return live_data
        else:
            print(f'Request Failed with status code {response.status_code}')
            return None

    def filter_shared_streams(self, live_data):
        live_data_filter = []
        if live_data and 'sharedLiveVideoStreams' in live_data:
            for live_stream in live_data['sharedLiveVideoStreams']:
                if 'test stream delete' in live_stream.get('name', '').lower(): #set to empty string to delete all unnamed streams
                    live_data_filter.append(live_stream)
        else:
            print('No shared live video streams found or the response is empty.')
        # pprint.pprint(live_data_filter)
        return live_data_filter  

    def delete_shared_streams(self):
        live_data = self.find_shared_streams()
        if not live_data:
            print('No Un-named streams')
            return

        live_data_filter = self.filter_shared_streams(live_data)  


        url = "https://api2.rhombussystems.com/api/camera/deleteSharedLiveVideoStream"

        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }

        for live_stream in live_data_filter:
            payload = {
                'cameraUuid': live_stream['cameraUuid'],
                'uuid': live_stream['uuid']
            }
            response = requests.post(url, json=payload, headers=headers)
            if response.status_code == 200:
                print(f'Stream with UUID {live_stream["uuid"]} deleted successfully')
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
            if "test" in wall.get("displayName").lower():
                uuid_dump.append(wall.get("uuid"))
        if not uuid_dump:
            print('No walls with display name test')
        pprint.pprint(uuid_dump)
        return uuid_dump 
    
    def delete_video_walls(self):
        delete_walls = self.get_video()
        if not delete_walls:
            print('No walls to delete')
            return
        uuid_dump = self.filter_wall(delete_walls)
    

        url = "https://api2.rhombussystems.com/api/camera/deleteVideoWall"

        payload = { "uuid": "" }
        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
}
        for uuid in uuid_dump:
            payload['uuid'] = uuid

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
        for id in role_data['permissionGroups']:
            if "sam".lower() in id['name']:
                role_dump.append(id['uuid'])
        pprint.pprint(role_dump)
        return role_dump 
    
    def delete_permission_group(self, role_dump):
        if not role_dump:
            print('no roles to delete')
            return
        
        url = "https://api2.rhombussystems.com/api/permission/deletePartnerPermissionGroup"

        headers = {
            "accept": "application/json",
            "x-auth-scheme": "api-token",
            "content-type": "application/json",
            "x-auth-apikey": "iMNxYzzsRjGYonqr2RwDYQ"
        }
        for uuid in role_dump:
            payload = {
                "uuid": uuid
            }
            response = requests.post(url, headers=headers)
            if response.status_code == 200:
                print(f'Role with uuid {uuid} was successfully deleted')
                return 
            else:
                print(f'Request failed with status code {response.status_code}')

                   

# for device_group in wall_json['deviceList']:
def run_cleanse():

    # camera_policies_instance = CameraPolicies()
    # filtered_data = camera_policies_instance.camera_policies()
    # camera_policies_instance.delete_policies()

    # solution = SharedStreams()
    # delete_live = solution.delete_shared_streams()

    # get_walls = GetVideoWall()
    # video_data = get_walls.get_video()
    # get_walls.filter_wall(video_data)
    # delete_walls = get_walls.delete_video_walls() ##DO NOT RUN WILL DELETE DEV WALLS

    permission_groups = GetRole()
    role_data = permission_groups.get_roles()
    permission_groups.filter_roles(role_data) 
    # permission_groups.delete_permission_group()

if __name__ == '__main__':
    run_cleanse()



    






