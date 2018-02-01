# Client

## Constructor
```py
import cocasync
client = cocasync.Client(token=token, timeout=timeout)
```
#### Variables
| Name | Description | Type |
|------|-------------|------|
| token | The authorization header for the [Clash of Clans API](https://developer.clashofclans.com/). | String |
| timeout | The timeout before aiohttp closes the request. | Integer |

## Variables
| Variable | Description | Type |
|----------|-------------|------|

## Methods
| Method | Description | Returns |
|--------|-------------|---------|
| getPlayer(tag) | Returns the player with the tag specified. | [Player](https://github.com/cree-py/cocasync/blob/master/documentation/PLAYER.md) |
| getLeagues() | Returns a list of all the Leagues in the game. | List of [League](https://github.com/cree-py/cocasync/blob/master/documentation/LEAGUE.md) |
| getLeague(league) | Returns a specific league. | [League](https://github.com/cree-py/cocasync/blob/master/documentation/LEAGUE.md) |
| getLeagueSeasons(league) | Returns a list of seasons for the league. | List of [GenericIDObject](https://github.com/cree-py/cocasync/blob/master/documentation/GENERICIDOBJECT.md) |
| getLeagueSeasonRanking(league, season) | Returns the ranking of league league for season season. | List of [RankedPlayer](https://github.com/cree-py/cocasync/blob/master/documentation/RANKEDPLAYER.md) |
| getLocations() | Returns all the locations clans can be set to in the game. | List of [Location](https://github.com/cree-py/cocasync/blob/master/documentation/LOCATION.md) |
| ~~searchForClans(search)~~ | ~~Searches for clans matching the search criteria~~ Coming soon! | List of [Clan](https://github.com/cree-py/cocasync/blob/master/documentation/CLAN.md) |
| getClan(tag) | Returns a clan with the tag specified. | [Clan](https://github.com/cree-py/cocasync/blob/master/documentation/CLAN.md) |
| getClanMembers(tag) | Returns the members in clan with tag tag. | List of [Player](https://github.com/cree-py/cocasync/blob/master/documentation/PLAYER.md) |
| getClanWarlog(tag) | Returns the log of the clan's most recent wars. | List of [WarlogItem](https://github.com/cree-py/cocasync/blob/master/documentation/WARLOGITEM.md) |
| getClanWar(tag) | Returns the clan's current ongoing war. | [WarlogItem](https://github.com/cree-py/cocasync/blob/master/documentation/WARLOGITEM.md) |