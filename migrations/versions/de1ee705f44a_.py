"""empty message

Revision ID: de1ee705f44a
Revises: 
Create Date: 2019-06-08 22:58:53.602637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'de1ee705f44a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('path', sa.String(length=80), nullable=True, comment='接口地址'),
    sa.Column('header', sa.String(length=80), nullable=True, comment='请求头'),
    sa.Column('method', sa.String(length=128), nullable=True, comment='请求方式'),
    sa.Column('data', sa.String(length=512), nullable=True, comment='接口参数'),
    sa.Column('status', sa.Integer(), nullable=True, comment='状态'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('case',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('name', sa.String(length=80), nullable=True, comment='用例名称'),
    sa.Column('comment', sa.String(length=512), nullable=True, comment='用例描述'),
    sa.Column('expect', sa.String(length=512), nullable=True, comment='期望响应结果'),
    sa.Column('response', sa.String(length=512), nullable=True, comment='实际响应结果'),
    sa.Column('status', sa.Integer(), nullable=True, comment='状态'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('logs',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('operation', sa.String(length=80), nullable=True, comment='操作描述'),
    sa.Column('operautor', sa.String(length=80), nullable=True, comment='操作人'),
    sa.Column('client', sa.Integer(), nullable=True, comment='最后操作的客户端'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('name', sa.String(length=80), nullable=True, comment='项目名称'),
    sa.Column('comment', sa.String(length=80), nullable=True, comment='项目描述'),
    sa.Column('status', sa.Integer(), nullable=True, comment='状态'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('role',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('role', sa.String(length=512), nullable=True, comment='用户角色'),
    sa.Column('description', sa.String(length=512), nullable=True, comment='中文含义'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('name', sa.String(length=128), nullable=True, comment='用户昵称'),
    sa.Column('username', sa.String(length=128), nullable=True, comment='用户名'),
    sa.Column('pwd_hash', sa.String(length=512), nullable=True, comment='密码'),
    sa.Column('status', sa.Integer(), nullable=True, comment='状态,0正常 1删除'),
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('variable',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('variable_name', sa.String(length=80), nullable=True, comment='变量名称'),
    sa.Column('script', sa.String(length=80), nullable=True, comment='脚本'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('webconfig',
    sa.Column('create_time', sa.DateTime(), nullable=True, comment='创建时间'),
    sa.Column('update_time', sa.DateTime(), nullable=True, comment='更新时间'),
    sa.Column('id', sa.Integer(), nullable=False, comment='主键'),
    sa.Column('name', sa.String(length=80), nullable=True, comment='配置名称'),
    sa.Column('url', sa.String(length=80), nullable=True, comment='环境地址'),
    sa.Column('header', sa.String(length=80), nullable=True, comment='公共请求头'),
    sa.Column('status', sa.Integer(), nullable=True, comment='状态'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('permissions',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('permissions')
    op.drop_table('webconfig')
    op.drop_table('variable')
    op.drop_table('user')
    op.drop_table('role')
    op.drop_table('project')
    op.drop_table('logs')
    op.drop_table('case')
    op.drop_table('api')
    # ### end Alembic commands ###
