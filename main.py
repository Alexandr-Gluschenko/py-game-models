import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for player_data in players_data:
        race, _ = Race.objects.get_or_create(name=player_data["race"])
        guild, _ = Guild.objects.get_or_create(name=player_data["guild"])

        skills = []
        for skill_data in player_data["skills"]:
            skill, _ = Skill.objects.get_or_create(name=skill_data["name"])
            skills.append(skill)

        player, _ = Player.objects.get_or_create(
            nickname=player_data["nickname"],
            guild=guild,
            race=race
        )
        player.skills.set(skills)
        player.save()


if __name__ == "__main__":
    main()