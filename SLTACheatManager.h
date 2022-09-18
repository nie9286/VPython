// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/CheatManager.h"
#include "SLTACheatManager.generated.h"

/**
 * 
 */
UCLASS()
class SLTA_API USLTACheatManager : public UCheatManager
{
	GENERATED_BODY()

	UFUNCTION(exec)
	void SLTA_DirectionalLighting_Dump();

	UFUNCTION(exec)
	void SLTA_SkyLight_Dump();

	UFUNCTION(exec)
	void SLTA_DirectionalLighting_SetIntensity(float intensity);

	UFUNCTION(exec)
	void SLTA_SkyLight_SetIntensity(float intensity);

	UFUNCTION(exec)
	void SLTA_Particle_Dump_EmitterInfo();

	//todo : Dump all particle component info......

};
