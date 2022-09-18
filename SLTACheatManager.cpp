// Fill out your copyright notice in the Description page of Project Settings.


#include "SLTACheatManager.h"
#include "Kismet/GamePlayStatics.h"
#include "Engine/DirectionalLight.h"
#include "Engine/SkyLight.h"
#include "Components/LightComponent.h"
#include "Components/SkyLightComponent.h"
#include "Particles/Emitter.h"
#include "Particles/ParticleSystemComponent.h"
#include "Particles/ParticleEmitter.h"
#include "Particles/ParticleLODLevel.h"
#include "Particles/ParticleModule.h"
#include "Particles/ParticleModuleRequired.h"
#include "Particles/Spawn/ParticleModuleSpawn.h"





void USLTACheatManager::SLTA_DirectionalLighting_Dump()
{
	auto playerController = GetOuterAPlayerController();
	if (playerController == nullptr)
	{
		UE_LOG(LogTemp, Error, TEXT("Get Invalid APlayerController"));
		return;
	}

	TArray<AActor*> lights;
	UGameplayStatics::GetAllActorsOfClass(playerController, ADirectionalLight::StaticClass(), lights);

	for (AActor* actor : lights)
	{
		ADirectionalLight* light = Cast<ADirectionalLight>(actor);
		auto lightComponent = light->GetLightComponent();
		UE_LOG(LogTemp, Warning, TEXT("========================================="));
		UE_LOG(LogTemp, Warning, TEXT("Name : %s"),*actor->GetName());
		UE_LOG(LogTemp, Warning, TEXT("Intensity : %f"),lightComponent->Intensity);
		UE_LOG(LogTemp, Warning, TEXT("Color : (%d,%d,%d)"), lightComponent->LightColor.R, lightComponent->LightColor.G, lightComponent->LightColor.B);
	}
}

void USLTACheatManager::SLTA_SkyLight_Dump()
{
	auto playerController = GetOuterAPlayerController();
	if (playerController == nullptr)
	{
		UE_LOG(LogTemp, Error, TEXT("Get Invalid APlayerController"));
		return;
	}

	TArray<AActor*> lights;
	UGameplayStatics::GetAllActorsOfClass(playerController, ASkyLight::StaticClass(), lights);
	for (AActor* actor : lights)
	{
		ASkyLight* light = Cast<ASkyLight>(actor);
		auto lightComponent = light->GetLightComponent();
		UE_LOG(LogTemp, Warning, TEXT("========================================="));
		UE_LOG(LogTemp, Warning, TEXT("Name : %s"), *actor->GetName());
		UE_LOG(LogTemp, Warning, TEXT("Intensity : %f"), lightComponent->Intensity);
		UE_LOG(LogTemp, Warning, TEXT("Color : (%d,%d,%d)"), lightComponent->LightColor.R, lightComponent->LightColor.G, lightComponent->LightColor.B);
	}

}

void USLTACheatManager::SLTA_DirectionalLighting_SetIntensity(float intensity)
{
	auto playerController = GetOuterAPlayerController();
	if (playerController == nullptr)
	{
		UE_LOG(LogTemp, Error, TEXT("Get Invalid APlayerController"));
		return;
	}

	TArray<AActor*> lights;
	UGameplayStatics::GetAllActorsOfClass(playerController, ADirectionalLight::StaticClass(), lights);

	for (AActor* actor : lights)
	{
		ADirectionalLight* light = Cast<ADirectionalLight>(actor);
		auto lightComponent = light->GetLightComponent();
		lightComponent->SetIntensity(intensity);
	}
}

void USLTACheatManager::SLTA_SkyLight_SetIntensity(float intensity)
{

	auto playerController = GetOuterAPlayerController();
	if (playerController == nullptr)
	{
		UE_LOG(LogTemp, Error, TEXT("Get Invalid APlayerController"));
		return;
	}

	TArray<AActor*> lights;
	UGameplayStatics::GetAllActorsOfClass(playerController, ASkyLight::StaticClass(), lights);
	for (AActor* actor : lights)
	{
		ASkyLight* light = Cast<ASkyLight>(actor);
		auto lightComponent = light->GetLightComponent();
		lightComponent->SetIntensity(intensity);
	}

}

void USLTACheatManager::SLTA_Particle_Dump_EmitterInfo()
{
	auto playerController = GetOuterAPlayerController();
	if (playerController == nullptr)
	{
		UE_LOG(LogTemp, Error, TEXT("Get Invalid APlayerController"));
		return;
	}

	UE_LOG(LogTemp, Warning, TEXT("====================Dump Particle====================="));

	TArray<AActor*> aemitters;
	UGameplayStatics::GetAllActorsOfClass(playerController, AEmitter::StaticClass(), aemitters);
	for (AActor* actor : aemitters)
	{
		AEmitter* emitter = Cast<AEmitter>(actor);
		auto pos = actor->GetActorLocation();
		UE_LOG(LogTemp, Warning, TEXT("AEmitter Name : %s | position : %f,%f,%f"), *actor->GetName(),pos.X,pos.Y,pos.Y);
		UE_LOG(LogTemp, Warning, TEXT("AEmitter Name : %s | position : %f,%f,%f"), *actor->GetName(), pos.X, pos.Y, pos.Y);

		auto particleSystemComponent = emitter->GetParticleSystemComponent();
		const auto templateAsset = particleSystemComponent->Template;
		const auto emitters = templateAsset->Emitters;
		for (auto emitter : emitters)
		{
			const auto lod = emitter->GetLODLevel(0);
			const auto requiredModeule = lod->RequiredModule;
			const auto spawnModule = lod->SpawnModule;
			//......
		}

	}
}

