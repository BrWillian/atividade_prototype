"""empty message

Revision ID: aabbc805ec9d
Revises: 
Create Date: 2023-06-23 16:01:16.457386

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aabbc805ec9d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('municipio',
    sa.Column('cod_municipio', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome_municipio', sa.String(), nullable=True),
    sa.Column('uf_municipio', sa.String(length=2), nullable=True),
    sa.PrimaryKeyConstraint('cod_municipio')
    )
    op.create_table('produto',
    sa.Column('cod_produto', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('desc_produto', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cod_produto')
    )
    op.create_table('propriedade',
    sa.Column('cod_propriedade', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome_propriedade', sa.String(), nullable=True),
    sa.Column('area', sa.Float(), nullable=True),
    sa.Column('distancia_municipio', sa.Float(), nullable=True),
    sa.Column('valor_aquisicao', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('cod_propriedade')
    )
    op.create_table('proprietario',
    sa.Column('cod_proprietario', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome_proprietario', sa.String(), nullable=True),
    sa.Column('fone1', sa.String(), nullable=True),
    sa.Column('fone2', sa.String(), nullable=True),
    sa.Column('fone3', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cod_proprietario')
    )
    op.create_table('pessoa_fisica',
    sa.Column('cod_prop_pf', sa.Integer(), nullable=False),
    sa.Column('cpf_prop', sa.Integer(), nullable=True),
    sa.Column('nome_pf', sa.String(), nullable=True),
    sa.Column('dt_nasc_pf', sa.Date(), nullable=True),
    sa.Column('rg_pf', sa.BigInteger(), nullable=True),
    sa.Column('cod_prop_conjuge', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cod_prop_conjuge'], ['pessoa_fisica.cod_prop_pf'], ),
    sa.ForeignKeyConstraint(['cod_prop_pf'], ['proprietario.cod_proprietario'], ),
    sa.PrimaryKeyConstraint('cod_prop_pf'),
    sa.UniqueConstraint('cpf_prop')
    )
    op.create_table('pessoa_juridica',
    sa.Column('cod_prop_pj', sa.Integer(), nullable=False),
    sa.Column('cnpj_prop', sa.Integer(), nullable=True),
    sa.Column('razao_social_pj', sa.String(), nullable=True),
    sa.Column('dt_cria_pj', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['cod_prop_pj'], ['proprietario.cod_proprietario'], ),
    sa.PrimaryKeyConstraint('cod_prop_pj'),
    sa.UniqueConstraint('cnpj_prop')
    )
    op.create_table('producao',
    sa.Column('cod_propriedade', sa.Integer(), nullable=False),
    sa.Column('cod_produto', sa.Integer(), nullable=False),
    sa.Column('mes_ini_colheita_prov', sa.Date(), nullable=True),
    sa.Column('mes_fin_colheita_prov', sa.Date(), nullable=True),
    sa.Column('qtd_prov_colheita', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('mes_ini_colheita_real', sa.Date(), nullable=True),
    sa.Column('mes_fin_colheita_real', sa.Date(), nullable=True),
    sa.Column('qtd_real_colhida', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.ForeignKeyConstraint(['cod_produto'], ['produto.cod_produto'], ),
    sa.ForeignKeyConstraint(['cod_propriedade'], ['propriedade.cod_propriedade'], ),
    sa.PrimaryKeyConstraint('cod_propriedade', 'cod_produto')
    )
    op.create_table('proprietario_propriedade',
    sa.Column('cod_propriedade', sa.Integer(), nullable=False),
    sa.Column('cod_proprietario', sa.Integer(), nullable=False),
    sa.Column('dt_aquisicao', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['cod_propriedade'], ['propriedade.cod_propriedade'], ),
    sa.ForeignKeyConstraint(['cod_proprietario'], ['proprietario.cod_proprietario'], ),
    sa.PrimaryKeyConstraint('cod_propriedade', 'cod_proprietario')
    )
    op.create_table('dono_pj',
    sa.Column('cod_prop_pj', sa.Integer(), nullable=False),
    sa.Column('cod_prop_pf', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cod_prop_pf'], ['pessoa_fisica.cod_prop_pf'], ),
    sa.ForeignKeyConstraint(['cod_prop_pj'], ['pessoa_juridica.cod_prop_pj'], ),
    sa.PrimaryKeyConstraint('cod_prop_pj', 'cod_prop_pf')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dono_pj')
    op.drop_table('proprietario_propriedade')
    op.drop_table('producao')
    op.drop_table('pessoa_juridica')
    op.drop_table('pessoa_fisica')
    op.drop_table('proprietario')
    op.drop_table('propriedade')
    op.drop_table('produto')
    op.drop_table('municipio')
    # ### end Alembic commands ###