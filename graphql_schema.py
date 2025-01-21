import strawberry
from graphql_classes import collect_resolver_classes

query_resolver_classes = collect_resolver_classes('queries')
mutation_resolver_classes = collect_resolver_classes('mutations')

@strawberry.type
class Query(*query_resolver_classes):
    pass

@strawberry.type
class Mutation(*mutation_resolver_classes):
    pass

schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)