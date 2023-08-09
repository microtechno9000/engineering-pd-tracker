"""add data to tables

Revision ID: 39dbded117d1
Revises: a644232fe039
Create Date: 2023-07-28 12:31:25.665683

"""
from alembic import op
from sqlalchemy import Integer, String, delete
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '39dbded117d1'
down_revision = 'a644232fe039'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Load in the training activity data

    training_activity = table(
        'training_activity',
        column('id', Integer),
        column('activity', String),
        column('description', String)
    )

    activity_list = [
        "Conference",
        "Exhibition",
        "Meeting",
        "Mentoring Session",
        "Online Study",
        "Other",
        "Presentation / Paper Preparation",
        "Private Study - book / manual",
        "Private Study - journal / magazine",
        "Private Study - research / web articles",
        "Seminar",
        "Technical Presentation",
        "Technical Site Visit",
        "Tertiary Study",
        "Training Course / session - external",
        "Training Course / session - workplace",
        "Volunteer Activity",
        "Workshop"
    ]

    activity_data = []
    for index, activity_name in enumerate(activity_list, start=1):
        activity = {
            "id": index,
            "activity": activity_name,
            "description": "Training activity covering " + activity_name
        }
        activity_data.append(activity)

    op.bulk_insert(
        training_activity, activity_data
    )

    # Load in the training type data
    training_type = table(
        'training_type',
        column('id', Integer),
        column('type', String),
        column('description', String),
        column('conditions', String)
    )

    type_list = [
        [
            "Type I",
            "Any tertiary courses taken either as an individual course or for a formal Post Graduate award.",
            "No Conditions"
        ],
        [
            "Type II",
            "Short courses, workshops, seminars and discussion groups, conferences, technical inspections and "
            "technical meetings, including Engineers Australia meetings, where these are delivered or facilitated by "
            "recognised practitioners in the field.",
            "No conditions."
        ],
        [
            "Type III",
            "Learning activities in the workplace that extend your area of practice competence base.",
            "A maximum of 75 hours of your total CPD in any three-year period may be claimed for these activities. "
            "The total claimable hours for learning activities in the workplace (Type III) and private study (Type IV) "
            "combined are 110 hours over three years"
        ],
        [
            "Type IV",
            "Private study which extends your knowledge and skills.",
            "Reading of the monthly Engineers Australia journal can contribute to a maximum of 18 hours of your total "
            "CPD for this Type in any three-year period. The total claimable hours for learning activities in the "
            "workplace (Type III) and private study (Type IV) combined are 110 hours over three years"
        ],
        [
            "Type V",
            "Service to the engineering profession",
            "A maximum of 50 hours of your total CPD in any three-year period may be claimed for these activities"
        ],
        [
            "Type VI",
            'The preparation and presentation of material for courses, conferences, seminars and symposia.',
            "Up to 45 hours for published papers. Maximum of 75 hours for papers subject to critical review."
        ],
        [
            "Type VII",
            "Chartered members employed in tertiary teaching and/or academic research.",
            "For Chartered members employed in tertiary teaching or academic research a minimum of 40 hours industry "
            "involvement is required."
        ],
        [
            "Type VIII",
            "Any other structured activities not covered by I-VII above that meet the objectives of the policy.",
            "The member is required to provide documentary justification for this type."
        ]
    ]

    type_data = []
    for index, type_row in enumerate(type_list, start=1):
        eatype = {
            "id": index,
            "type": type_row[0],
            "description": type_row[1],
            "conditions": type_row[2]
        }
        type_data.append(eatype)

    op.bulk_insert(
        training_type, type_data
    )

    # Load in the training EA Division
    training_division = table(
        'training_division',
        column('id', Integer),
        column('division', String)
    )

    division_list = [
        "National",
        "Non-EA Event",
        "Canberra",
        "Newcastle",
        "Northern Territory",
        "Queensland",
        "South Australia",
        "Sydney",
        "Tasmania",
        "Victoria",
        "Western Australia"
    ]

    division_data = []
    for index, division_row in enumerate(division_list, start=1):
        division = {
            "id": index,
            "division": division_row
        }
        division_data.append(division)

    op.bulk_insert(
        training_division, division_data
    )


def downgrade() -> None:
    training_activity = table(
        'training_activity',
        column('id', Integer),
        column('activity', String),
        column('description', String)
    )
    training_type = table(
        'training_type',
        column('id', Integer),
        column('type', String),
        column('description', String),
        column('conditions', String)
    )
    training_division = table(
        'training_division',
        column('id', Integer),
        column('division', String)
    )
    delete(training_activity).where(training_activity.id == "*")
    delete(training_type).where(training_type.id == "*")
    delete(training_division).where(training_division.id == "*")
