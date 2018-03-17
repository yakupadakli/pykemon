# -*- coding: utf-8 -*-

from beckett.resources import BaseResource


class Resource(BaseResource):

    @staticmethod
    def get_single_resource_url(url, uid, **kwargs):
        # Needs a slash on the end!
        return '{}/{}/'.format(url, uid)


class PokemonResource(Resource):

    class Meta(BaseResource.Meta):
        name = 'Pokemon'
        resource_name = 'pokemon'
        attributes = (
            'created',
            'modified',
            'national_id',
            'abilities',
            'egg_groups',
            'evolutions',
            'descriptions',
            'moves',
            'types',
            'catch_rate',
            'species',
            'hp',
            'attack',
            'defense',
            'name',
            'sp_atk',
            'sp_def',
            'speed',
            'total',
            'egg_cycles',
            'ev_yield',
            'exp',
            'growth_rate',
            'height',
            'weight',
            'happiness',
            'male_female_ratio',
            'sprites',
        )


class MoveResource(Resource):

    class Meta(BaseResource.Meta):
        name = 'Move'
        resource_name = 'move'
        attributes = (
            'created',
            'modified',
            'id',
            'accuracy',
            'category',
            'power',
            'pp',
            'name',
        )


class TypeResource(Resource):

    class Meta(BaseResource.Meta):
        name = 'Type'
        resource_name = 'type'
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'ineffective',
            'resistance',
            'super_effective',
            'weakness',
        )


class AbilityResource(Resource):

    class Meta(BaseResource.Meta):
        name = 'Ability'
        resource_name = 'ability'
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'description',
        )


class EggResource(Resource):

    class Meta(BaseResource.Meta):
        name = 'Egg'
        resource_name = 'egg'
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'pokemon',
        )


class DescriptionResource(Resource):

    class Meta(BaseResource.Meta):
        name = 'Description'
        resource_name = 'description'
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'description',
            'pokemon',
            'games',
        )


class SpriteResource(Resource):

    class Meta(BaseResource.Meta):
        name = 'Sprite'
        resource_name = 'sprite'
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'pokemon',
            'image',
        )


class GameResource(Resource):

    class Meta(BaseResource.Meta):
        name = 'Game'
        resource_name = 'game'
        attributes = (
            'created',
            'modified',
            'id',
            'name',
            'generation',
            'release_year',
        )
