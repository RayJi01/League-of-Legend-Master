# Copyright 2023-2024 Rui Ji at Ruiji@copyright
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests

API_KEYS = "RGAPI-41d8011c-1cf6-4c4f-a0c8-edab3b798536"  # this has to be change every day


class Summoner:
    """
    The Constructor of the Summoner Class, instantiate the basic identifier and information

    Parameters:
        name (string): the required summoner name
        region (string): the region of server the summoner in (na1, eu, etc)

    Returns:
        None
    """
    def __init__(self, name, region):
        api_url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}"
        total_request = api_url + "?api_key=" + API_KEYS
        resp = requests.get(total_request)
        json_dict = resp.json()

        self.summoner_id = json_dict['id']
        self.summoner_accountID = json_dict['id']
        self.summoner_puuid = json_dict['puuid']
        self.summoner_name = json_dict['name']
        self.summoner_profileIconID = json_dict['profileIconId']
        self.summoner_revisionDate = json_dict['revisionDate']
        self.summoner_level = int(json_dict['summonerLevel'])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_instance = Summoner("eiduiwk", "na1")
    print(new_instance.summoner_revisionDate)
