import json

from db.models import Race, Skill, Player, Guild


def main() -> None:
    with open("players.json", "r") as f:
        players_data = json.load(f)

    for player_data in players_data:
        guild, created = Guild.objects.get_or_create(name=player_data["guild"])

        race, created = Race.objects.get_or_create(name=players_data["race"])

    skills = []
    for skill_data in players_data["skills"]:
        skill, created = Skill.objects.get_or_create(name=skill_data["name"])
        skills.append(skill)

    player, created = Player.objects.get_or_create(
        name=players_data["name"],
        guild=guild,
        race=race
    )
    player.skills.set(skills)
    player.save()

if __name__ == "__main__":
    main()