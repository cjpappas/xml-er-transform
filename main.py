import xml.etree.ElementTree as ET
import sys

def main(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    print(get_entities(root))
    print(get_relationships(root))
    logical_transform(get_entities(root), get_relationships(root))

def get_entities(root):
    entities = []
    for e in root.find('entities'):
        entity = e.attrib
        entity['attributes'] = [a.attrib for a in e.findall('attribute')]
        entities.append(entity)
    return entities

def get_entity_with_id(entities, id):
    for entity in entities:
        if entity['id'] == id:
            return entity

def get_relationships(root):
    return [r.attrib for r in root.find('relationships')]

def get_primary_key(entity):
    for attribute in entity['attributes']:
        if attribute['pi'] == 'true':
            return attribute['value']

def get_relation_from_entity(relations, entity):
    for relation in relations:
        if entity['name'] in relation.keys():
            return relation

"""
Performs steps in the logical transformation
"""
def logical_transform(entities, relationships):
    relations = step_1(entities)
    pretty_print_relations(step_4(entities, relationships, relations))

"""
Performs the first step in the logical transformation, which is to create a relation
for each *strong* entity, where composite attributes are expanded and multi-value
attributes are excluded.

Paramters:
    entities (list(entity)): A list of dictionaries representing entities.

Returns:
    relations (list(relation)): A list of relations (tables)
"""
def step_1(entities):
    relations = []
    for entity in entities:
        simple_attributes = list(map(lambda a : a['value'], entity['attributes']))
        relations.append({ entity['name'] : simple_attributes })
    return relations

"""
For each binary 1 TO N Relationship identify the relations that represent the participating entity at the N (i.e many) side of the relationship. Include as foreign key in the relation that holds the N side, the primary key of the other entity (that holds the 1 side).
"""
def step_4(entities, relationships, relations):
    for relationship in relationships:
        if relationship['value'] == 'one-many':
            # Put customer (from) pk as fk in order (to)
            foreign_key = get_primary_key(get_entity_with_id(entities, relationship['fromEnt']))
            relation = get_relation_from_entity(relations, get_entity_with_id(entities, relationship['toEnt']))
            relation[list(relation.keys())[0]].append(foreign_key)
    return relations


def pretty_print_relations(relations):
    for r in relations:
        for (name, attributes) in r.items():    
            print("%s(%s)"%(name.upper(), ', '.join(attributes)))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("You have not provided a file.")
    else:
        main(sys.argv[1])