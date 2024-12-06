/*
  Warnings:

  - You are about to drop the `GenomeScore` table. If the table is not empty, all the data it contains will be lost.
  - You are about to drop the `GenomeTag` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "GenomeScore" DROP CONSTRAINT "GenomeScore_movieId_fkey";

-- DropForeignKey
ALTER TABLE "GenomeScore" DROP CONSTRAINT "GenomeScore_tagId_fkey";

-- DropTable
DROP TABLE "GenomeScore";

-- DropTable
DROP TABLE "GenomeTag";
