# Clan

## Variables
| Variable | Description | Type |
|----------|-------------|------|
| tag | The clan's tag. | String |
| name | The clan's name. | String |
| clanLevel | The clan's level. | Integer |
| clanPoints | The amount of points the clan has. | Integer |
| clanVersusPoints | The amount of versus points the clan has. | Integer |
| members | The amount of members in the clan. | Integer |
| type | The type of the clan. | String |
| requiredTrophies | The minimum amount of trophies required for a player in order to join the clan. | Integer |
| warFrequency | How often the clan participates in Clan Wars. | String |
| warWinStreak | The clan's current win streak for wars. | Integer |
| warWins | How many times the clan has won a war. | Integer |
| warTies | How many times the clan has tied a war. | Integer |
| warLosses | How many times the clan has lost a war. | Integer |
| description | The clan's description. | String |
| isWarLogPublic | Is the warlog public? | Boolean |

## Methods
| Method | Description | Returns |
|--------|-------------|---------|
| getLocation() | Returns the set location of the clan. | [Location](https://github.com/cree-py/cocasync/blob/master/documentation/LOCATION.md) |
| getBadges() | Returns a list of the URLs for the clan's badge. | List of [UrlList](https://github.com/cree-py/cocasync/blob/master/documentation/URLLIST.md) |
| getMembers() | Returns a list of members in the clan. | List of [Player](https://github.com/cree-py/cocasync/blob/master/documentation/PLAYER.md) |