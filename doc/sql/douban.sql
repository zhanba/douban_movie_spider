/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2016/9/28 10:28:44                           */
/*==============================================================*/


drop index Index_tags on movie;

drop index Index_rating_num on movie;

drop index Index_actors on movie;

drop index Index_directors on movie;

drop index Index_year on movie;

drop index Index_name on movie;

drop table if exists movie;

/*==============================================================*/
/* Table: movie                                                 */
/*==============================================================*/
create table movie
(
   uuid                 char(36) not null,
   subject_id           varchar(50) not null,
   name                 varchar(1000) not null,
   year                 int,
   cover_url            varchar(1000),
   directors            varchar(1000),
   writers              varchar(1000),
   actors               varchar(1000),
   genres               varchar(1000),
   countries            varchar(1000),
   languages            varchar(200),
   release_date         varchar(100),
   running_time         int,
   alias                varchar(1000),
   imdb_link            varchar(100),
   rating_num           float,
   rating_people        bigint,
   summary              text,
   tags                 varchar(1000),
   primary key (uuid)
)
type = InnoDB;

/*==============================================================*/
/* Index: Index_name                                            */
/*==============================================================*/
create index Index_name on movie
(
   name
);

/*==============================================================*/
/* Index: Index_year                                            */
/*==============================================================*/
create index Index_year on movie
(
   year
);

/*==============================================================*/
/* Index: Index_directors                                       */
/*==============================================================*/
create index Index_directors on movie
(
   directors
);

/*==============================================================*/
/* Index: Index_actors                                          */
/*==============================================================*/
create index Index_actors on movie
(
   actors
);

/*==============================================================*/
/* Index: Index_rating_num                                      */
/*==============================================================*/
create index Index_rating_num on movie
(
   rating_num
);

/*==============================================================*/
/* Index: Index_tags                                            */
/*==============================================================*/
create index Index_tags on movie
(
   tags
);

